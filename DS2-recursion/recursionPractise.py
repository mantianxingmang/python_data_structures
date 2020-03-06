#可视化递归算法
import turtle

# myTurtle = turtle.Turtle()
# myScreen = turtle.Screen()

# def drawSpiral(myTurtle, lineLen):
#     if lineLen > 0:
#         myTurtle.forward(lineLen)
#         myTurtle.right(90)
#         drawSpiral(myTurtle,lineLen - 5)

# drawSpiral(myTurtle,100)
# myScreen.exitonclick() 


def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(45)
        tree(branchLen-15,t)
        t.left(90)
        tree(branchLen-15,t)
        t.right(45)
        t.backward(branchLen)

def main():
    t = turtle.Turtle()
    myScreen = turtle.Screen()

    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("red")
    tree(75,t)
    myScreen.exitonclick()

main()

from pythonds.basic.stack import Stack

def moveTower(height,fromPole,toPole,withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

def moveDisk(fp,tp):
    print("移动盘子，从",fp,"到",tp)

fromPole = Stack()
toPole = Stack()
withPole = Stack()

moveTower(5,fromPole,toPole,withPole)
