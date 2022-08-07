import random


def pick_animal():
    picked_animal = []
    animals = ['사자', '호랑이', '코끼리', '뱀', '고양이', '고래', '낙타']
    while True:
        picked = random.choice(animals)
        yield picked
        picked_animal.append(picked)
        print(len(picked_animal))
       


# animal = pick_animal()  # 제너레이터 생성

# print(animal.__next__())    # 값 출력
# print(next(animal))
# print(next(animal))
# print(next(animal))

# for animal in pick_animal():
#     print(animal)
    
#     if len(animal) == 1:
#         break


def animal_generator():
    yield from pick_animal()

animal = animal_generator()

print("첫번째",animal.__next__())    # 값 출력
print("두번째",next(animal))
print("세번째",next(animal))
print("네번째",next(animal))


list_comp = [i for i in range(1, 11)]
gen_comp = (i for i in range(1, 11))

print(list_comp)
print(gen_comp)

a = next(gen_comp)
print(a)