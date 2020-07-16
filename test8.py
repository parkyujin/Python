# 랜덤 함수        # 쓰고자 하는 함수가 설치가 안되어있으면 가져와야 한다.
import os
# print(os.listdir("c:/windows"))

from random import randint
from random import random
from random import randrange

a = randint(10, 19)
b = randrange(1, 10, 2)
print(a, b)

# a = random() 0.0 ~ 1.0 미만
# a = random() * 10 # 0.0 ~ 10.0 미만
# a = int(random() * 10)
# a = randint(10, 19) # 10 ~ 20 미만
### for i in range(1, 5)

from random import random

num = int(random() * 100)

if num > 50:
    print("50보다 크다!")
if num <= 50 :
    print("50보다 작거나 같아요")

if num % 2 == 0 :
    print("num은 짝수입니다!")
elif num % 2 == 1 :
    print("num은 홀수입니다!")

forecast = int(input("오늘 비가 올 확률은 몇 %인가요? : "))
if forecast >= 50 :
    print("우산을 준비하세요!")
else:
    print("친구를 만나세요!")


weather = input("오늘 날씨 어때요?(맑음, 비, 눈, 흐림, 안개, 미세먼지) : ")

if weather in ("눈, 비") :
    print("우산을 준비하세요")
elif weather in ("안개, 미세먼지") :
    print("마스크 준비하세요")
elif weather == '맑음' :
    print("친구를 만나세요")
else:
    print("Stay home")