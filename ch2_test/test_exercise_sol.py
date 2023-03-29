
# print("hello lsy")
# print("dd")
# n1 = 10
# n2 = 5
# print(n1,"*",n2,"=",n1*n2)
# print(Str(n1)+"*"+Str(n2)+"="+n1*n2)

# n1 = int(input("숫자1-->"))
# n2 = int(input("숫자2-->"))
# n3 = int(input("숫자3-->"))
# res = n1 + n2 + n3 
# res2 = n1 * n2 * n3
# print(n1,"+",n2,"+",n3,"=",res)
# print(n1,"*",n2,"*",n3,"=",res2)

import turtle
import random

# 왼쪽클릭으로 클릭 위치까지 임의의 색상 그리면서 이동한 후, 
# 임의의 크기 및 각도의 거북이 도장 찍히는 프로그램.
def screenLeftClick(x,y):
  global r,g,b 

  r = random.random()
  g = random.random()
  b = random.random()
  turtle.pencolor((r,g,b))
  turtle.pendown()
  turtle.goto(x,y)
  tSize = random.randrange(1,10)   
  turtle.shapesize(tSize)
  angleRandom = random.randrange(1,361)
  turtle.right(angleRandom)
  turtle.stamp()

# def screenRightClick(x,y):
#   turtle.penup()
#   turtle.goto(x,y)

# def screenMidClick(x,y):
#   global r,g,b 
#   tSize = random.randrange(1,10)   
#   turtle.shapesize(tSize)
#   r = random.random()
#   g = random.random()
#   b = random.random()

pSize = 10 

# r, g, b = 0.0 , 0.0 , 0.0 

turtle.title('test')
turtle.shape('turtle')
turtle.pensize(pSize)


turtle.onscreenclick(screenLeftClick,1)
# turtle.onscreenclick(screenMidClick,2)
# turtle.onscreenclick(screenRightClick,3)

turtle.done()