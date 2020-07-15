import turtle               # import 는 외부 모듈을 사용하기 위해 선언한다.
import random

# 함수 선언 부분
'''
def screenLeftClick(x,y) :
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x,y)

def screenRightClick(x,y) : 
    turtle.penup()
    turtle.goto(x,y)

def screenMidClick(x, y) :
    global r,g,b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
'''
def screenLeftClick(x,y) :
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x,y)

def screenRightClick(x,y) : 
    turtle.penup()
    turtle.goto(x,y)

    global r,g,b
    tSize = random.randrange(1, 10)
    turtle.shapesize(tSize)
    r = random.random()
    g = random.random()
    b = random.random()
                                        ## Mid 클릭과 Right 클릭의 기능을 합친 함수.

# 변수 선언 부분
pSize = 10
r, g, b = 0.0, 0.0, 0.0

# 메인 코드 부분
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')                      # classic ,triangle 등등 으로도 변경 가능 
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
#turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
