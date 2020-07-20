'''
fruit = ['사과', '배', '딸기', '포도']
print(fruit)

fruit.append('귤')
print(fruit)

if '감' in fruit :          # if '항목' : fruit 에 항목이 있다면 조건이 충족되어 조건문이 실행
    print("아마 배는 없겠지.")

'''

import random

numbers = []
for num in range(0, 10) :
    numbers.append(random.randrange(0, 10))

print("생성된 리스트", numbers)

for num in range(0, 10):
    if num not in numbers :
        print("숫자 %d는 리스트에 없습니다." %num)


for num in range(0, 10) :
    if num in numbers :
        print("숫자 %d는 리스트에 있습니다." %num)