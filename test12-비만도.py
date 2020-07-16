weight = int(input("몸무게를 입력해주세요 : "))
height = int(input("키를 입력해주세요 : "))

std = height*height*21.5*0.0001
BMD = (weight - std)/std*100

print("당신의 비만지수는 %f 로" %BMD)

if BMD < -10 :
    print("저체중입니다.")
else :
    if BMD < 10 :
        print("정상체중입니다.")
    else :
        if BMD < 20 :
            print("비만입니다.")
        else :
            print("고도비만입니다.")
# 인터넷이랑 같게 안나온다 계산법이 잘못된것같다. 그만하고싶다. 안녕 빠이
'''
if BMD < 100 :
    print("저체중입니다.")
else :
    if BMD < 110 :
        print("정상입니다.")
    else :
        if BMD < 120 :
            print("과체중입니다.")
        else :
            if BMD < 130 :
                print("비만입니다.")
            else :
                print("고도비만입니다.")
'''