
num1, num2 = 10, 20
name, age = 'Yujin', 25

print('{} + {} = {}' .format(num1, num2, num1 + num2))
print('이름 : {} \n나이 : {}'.format(name, age))


english, math, korean = 100 , 50, 100
tot = english + math + korean
avg = tot / 3
print('합계 : {}\n평균 : {:.2f}'.format(tot, avg)) 

# input 함수
m1 = input("Message : ")
print(m1)