import turtle

## 전역 변수부
num = 0
swidth , sheight = 1000, 300
curX, curY = 0, 0

# 메인 코드부
if __name__ == "__main__" :
    turtle.title('거북이로 2진수 표현하기')
    turtle.shape('turtle')
    turtle.setup(width = swidth + 50, height = sheight + 50)
    turtle.screensize(swidth, sheight)
    turtle.penup()
    turtle.left(90)

    num = int(input("숫자를 입력하세요 : "))
    binary = bin(num)       # 입력한 숫자를 2진수로 변환한다.
    curX = swidth / 2       # 거북이 위치의 X 좌표
    curY = 0                # 거북이 위치의 Y 좌표
    for i in range(len(binary)-2) : # 변환된 2진수의 길이 만큼 반복한다. -2는 앞에 0b를 제외한 것.
        turtle.goto(curX, curY)     # 알맞은 값의 좌표로 이동한다.
        if num & 1 :
            turtle.color('red')
            turtle.turtlesize(2)
        else :
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()  # 거북이 도장을 현재 위치에 찍는다.
        curX -= 50      # 거북이를 왼쪽으로 50만큼 이동시킨다.
        num >>= 1       # 맨 오른쪽 비트에 대한 도장을 찍었으니 다른 비트를 찍으러가보자.

turtle.done()