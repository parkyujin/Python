import turtle
import random

# 전역 변수 선언부
swidth, sheight, pSize, exitCount = 300, 300, 170, 0
r, g, b, angle, dist, curX, curY = [0] * 7

# 메인 코드부
turtle.title('거북이가 마음대로 다니기')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width = swidth + 30, height = sheight + 30)        # 윈도창 크기 지정
turtle.screensize(swidth, sheight)                              # 안쪽 화면 크기 지정

while True :
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))

    angle = random.randrange(0, 360)
    dist = random.randrange(1, 100)
    turtle.left(angle)
    turtle.forward(dist)
    curX = turtle.xcor()                ## 거북이의 현재 위치를 구한다.
    curY = turtle.ycor()

    if (-swidth / 2 <= curX and curX <= swidth / 2) and (-sheight / 2 <= curY and curY <= sheight / 2) :          ##거북이의 현재 위치가 화면 안인지 체크.
        pass        # 거북이가 좌표 안에 있으면 pass
    else :          # 범위를 벗어난다면 실행
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()

        exitCount += 1
        if exitCount >= 10000 :
            break

turtle.done()