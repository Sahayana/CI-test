import random
from collections import deque

COUPONS = (500, 1000, 2000, 3000, 10000)
COUPONS_WITHOUT_500 = (1000, 2000, 3000, 10000)


def rullet_gen():
    last_coupons = deque(maxlen=2)  # 함수 local 변수
    while True:
        picked = random.choice(COUPONS)
        if picked == 500 and last_coupons.count(500) == 2:
            picked = random.choice(COUPONS_WITHOUT_500)  #  3연속 500원 금지!
        last_coupons.append(picked)
        yield picked


# # client 코드
# for coupon in rullet_gen():  # 호출하는 쪽에서는 이렇게나 쉽게 사용할 수 있답니다!
#     print(coupon)

'''
- 함수 안에 yield 가 한 번이라도 등장하면 generator 함수 입니다.
- generator 함수를 실행하면 함수가 실행되는 대신 generator 객체를 리턴합니다.
- generator 의 `__next__()` 함수를 실행하면 함수 본문이 실행됩니다.
- 함수 본문 실행 중에 yield 를 만나면 일시정지 합니다.
- generator 는 함수가 실행되고 있는 환경을 그대로 저장한 상태로 함수를 "일시정지" 시킵니다. 따라서 일시정지 할 때 함수의 local 변수도 그대로 저장되어 있으며 다시 함수를 실행할 때 local 변수를 그대로 사용할 수 있습니다.
'''

rullet1 = rullet_gen()
rullet2 = rullet_gen()
rullet3 = rullet_gen()

rullets = deque([rullet1, rullet2, rullet3])


while rullets:  # generator 의 실행을 책임지고 있습니다.
    rullet = rullets.popleft()
    print(rullet.__next__())
    print(rullet.__next__())

