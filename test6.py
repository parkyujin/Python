a = input("물건의 A무게?")
b = input("물건의 B무게?")

aw = 600 - int(a) - int(b)
print('화물 엘레베이터의 무게는 {:.2f}kg 남았습니다.'.format(aw))


