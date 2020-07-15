
name = input('이름을 입력하세요 : ')
height = int(input('키를 입력하세요 : '))
weight = int(input('몸무게를 입력하세요 : '))
standard = (height - 100) * 0.9
BMI = weight / standard * 100

print('{}님의 비만도는 {:.2f}% 입니다.'.format(name, BMI))

'''
name, height, weight = input('이름을 입력하세요 : '), int(input('키를 입력하세요 : ')), int(input('몸무게를 입력하세요 : '))

print('{}님의 비만도는 {:.2f}% 입니다.'.format(name, weight/(height-100)*0.9*100))

'''
