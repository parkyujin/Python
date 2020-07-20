'''
for i in range(0, 100) :
    print(i)

for i in range(0, 100) :            # 2로 나눠서 나머지가 0인 i 값만 출력.
    if i % 2 == 0 :
        print(i)


for i in range(0, 100, 20) :        # 20씩 띄어서 출력할 수 있음.
    print (i, end='/')              # 한 줄에, i 값 사이에 / 넣어서 출력.
'''

# 랜덤으로 숫자 더해서 출력하기.
from random import randint

hap = 0                     # 원래는 선언을 하지 않아도 되지만, 뭔가를 더하려면 값이 있긴 있어야 됨.
for i in range(0, 10) :     # 9번 반복
    rand = randint(0, 100)  # 임의의 숫자 9번을 더함.
    hap = hap + rand        # rand 값을 9번 더하기 위해 값을 저장할 변수가 필요.
print(hap)
