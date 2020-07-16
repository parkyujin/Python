import turtle

# 전역 변수 선언부
swidth, sheight = 500, 500

# 메인 코드부
turtle.title('무지개색 원그리기')
turtle.shape('turtle')
turtle.setup(width = swidth, height = sheight) # 
turtle.screensize(swidth, sheight)
turtle.penup()
turtle.goto(0, -sheight / 2)        # 0은 윈도창의 정중앙. sheight는 창전체의 맨 위.
turtle.pendown()
turtle.speed(0)

for radius in range(1, 250) :
    if radius % 7 == 1 :
        turtle.pencolor('red')
    elif radius % 7 == 2 :
        turtle.pencolor('orange')
    elif radius % 7 == 3 :
        turtle.pencolor('yellow')
    elif radius % 7 == 4 :
        turtle.pencolor('green')
    elif radius % 7 == 5 :
        turtle.pencolor('blue')
    elif radius % 7 == 6 :
        turtle.pencolor('navyblue')
    else :
        turtle.pencolor('purple')   # 반지름 1에서 249까지 원을 그리는데 나머지에 따라 색이 변함.

    turtle.circle(radius)       # 거북이가 원을 그리는 함수

turtle.done()        
        
    