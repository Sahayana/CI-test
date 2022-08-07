import random
from collections import deque

COUPONS = (500, 1000, 2000, 3000, 10000)
COUPONS_WITHOUT_500 = (1000, 2000, 3000, 10000)


def rullet(last_coupons):
    picked = random.choice(COUPONS)
    if picked == 500 and last_coupons.count(500) == 2:
        picked = random.choice(COUPONS_WITHOUT_500)  # 3연속 500원 금지!
    last_coupons.append(picked)
    return picked

# client 코드 (rullet()을 호출하는 코드)
last_coupons = deque(maxlen=2)
while True:
    picked = rullet(last_coupons)
    print(picked)


'''
함수가 실행을 종료하면 local 변수는 전부 제거되버리기 때문에, last_coupons 는 함수 밖에 저장할 수 밖에 없습니다. 호출하는 쪽에서 변수 last_coupons 를 관리하는 책임을 지게 됩니다.

이 불편함을 없애기 위해서 파이썬 커뮤니티에서 고민을 많이 했다고 하는데요

- iterator 를 구현합니다. -> 일반 함수보다 상대적으로 복잡한 iterator 클래스를 구현해야 합니다. 그렇지만 함수 외부에서 정보(last_coupons)를 관리해야 함은 변함이 없습니다.
- last_coupons 자료구조를 전달하는 대신 check 를 담당하는 함수를 인자로 전달합니다. -> 이 역시 `rullet()` 함수 외부에서 정보(last_coupons)를 관리해야 함은 변함이 없습니다.
'''


