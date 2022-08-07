import time
import asyncio
import datetime
import random




# def num_coroutine():
#     x = 0
#     while True:        
#         x = (yield x)
        

# co = num_coroutine()

# print(co.__next__())

# print(co.send(1))
# print(co.send(2))
# print(co.send(3))

def exit_coroutine():
    print(f"시작시간: {time.strftime('%X')}")
    try:
        while True:
            x = (yield)
            print(x, end=' ')
    except GeneratorExit:
        print('코루틴 종료')
        print(f"종료시간: {time.strftime('%X')}")

co2 = exit_coroutine()

co2.__next__()

for i in range(1, 21):
    co2.send(i)

co2.close()




async def display_date(num, loop):
    end_time = loop.time() + 50.0
    while True:
        print("Loop: {} Time: {}".format(num, datetime.datetime.now()))
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(random.randint(0, 5))
 
 
loop = asyncio.get_event_loop()
 
asyncio.ensure_future(display_date(1, loop))
asyncio.ensure_future(display_date(2, loop))
 
loop.run_forever()


