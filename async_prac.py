import asyncio
import time


async def hi(sleep_time: int, message: str):
    print(f"start {sleep_time} {message}")
    print(f'scheduled: {asyncio.get_event_loop()._scheduled}')  # 바로 실행이 안되는 코루틴은 _scheduled(heap)에 저장 및 대기 후 _ready로 들어가서 실행
    print(f'ready: : {asyncio.get_event_loop()._ready}')    # 바로 실행이 가능한 코루틴은 _ready(deque)에 저장되어 차례대로 실행
    await asyncio.sleep(sleep_time) # await문을 만나면 안의 코루틴을 _scheduled에 등록 (start 2 지점에 _scheduled에 TimeHandler 객체 1개가 저장되어 있는 것을 볼 수 있음)
    print(f"end {sleep_time} {message}")
    print(f'scheduled: {asyncio.get_event_loop()._scheduled}')


async def main():
    print(f"started main at {time.strftime('%X')}")
    coros = [hi(i, str(i)) for i in range(1, 11)]
    await asyncio.gather(*coros)
    print(f"finished main at {time.strftime('%X')}")


asyncio.run(main())

'''
- 함수 본문에 `yield` 가 들어가면 제너레이터 함수가 되었던 것 처럼, 함수 정의가 `async def` 로 시작하면 `코루틴`이 됩니다.
- `async` 키워드가 붙은 함수를 호출하면 함수가 실행되는 대신 코루틴 객체가 리턴됩니다. (제너레이터 함수가 제너레이터를 리턴하는 것 처럼)
- `async` 키워드가 붙은 함수 안에서는 `await` 을 사용할 수 있습니다. (generator 함수 안에서 yield 를 사용했던 것 처럼
- 함수 실행 중 `await` 을 만나면 다음과 같은 일이 일어납니다:
    1. await 문의 코루틴을 이벤트 루프에 등록합니다. 
    2. 실행 컨텍스트가 이벤트 루프 안의 다른 코루틴 객체에게 넘어갑니다. (제너레이터가 yield 를 만나면 반환하고 멈추는 것 처럼)
    
    이벤트 루프에 등록했던 코루틴이 실행 완료 되면, 다시 실행을 재개합니다. (제너레이터가 일시정지 되었다 다시 실행되는 것처럼)
    
- 이벤트 루프는 루프 안의 코루틴을 차례대로 실행합니다.
- 어떤 조건에 의해 await 이 끝나면 (예제에서는 `asyncio.sleep()` 을 사용했으므로 시간이 지나면 await 이 끝납니다.) await 이후 문장부터 다시 실행합니다. (제너레이터가 yield 이후 다시 실행되는 것 처럼)

코루틴을 이해할 때에는 generator 에는 없었던 event_loop 의 개념이 있습니다. event_loop 는 코루틴을 등록받고, 실행하는 역할을 담당합니다.

'''