# def tostr (n,base):
#   converstring = '0123456789ABCDEF'
#   if n<base :
#     return converstring[n]
#   else:
#     return tostr(n//base,base)+converstring[n%base]
#   # n//base 取整 n%base 取余

import turtle
t = turtle.Turtle()

# t.pencolor('red')
# t.pensize(3)
# def drawSpiral(t,linelen):
#   if linelen>0:
#     t.forward(linelen)
#     t.right(90)
#     drawSpiral(t,linelen-3)
# drawSpiral(t,20)
# turtle.done()
t.pencolor('red')
t.pensize(3)

def tree (branch):
  if branch>5:
    t.forward(branch)
    t.right(20)
    tree(branch-10)
    t.left(40)
    tree(branch-10)
    t.right(20)
    t.backward(branch)

t.left(90)
t.penup()
t.backward(100)
t.pendown()
tree(40)
turtle.done()
