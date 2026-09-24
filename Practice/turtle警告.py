import turtle
import math

t = turtle.Turtle()
n = int(input())

#基础设置
t.color('black')
t.pensize(16)
t.fillcolor('yellow')
t.speed(8)

#画出三角形并填色
t.begin_fill()         # 在绘制需要填充颜色的形状之前调用
while True:
	t.forward(n)
	t.left(120)
	if abs(t.pos()) < 1:  # t.pos() 返回海龟当前的坐标 
		break
t.end_fill()

#开始进行感叹号的设计
h = math.sqrt(3) / 2 * n
cx = n / 2
length = h * 0.35
steps = 40

t.penup()
t.goto(cx, h * 0.62)
t.setheading(270)      # 朝下
t.pendown()

for i in range(steps):
    width = n * 0.12 * (1 - 0.7 * i / steps)
    t.pensize(width)
    t.forward(length / steps)

# 感叹号的圆点
t.penup()
t.goto(cx, h * 0.16)       # 圆点位置跟 n 有关
t.dot(n * 0.12, "black") 

t.hideturtle()		   # 隐藏海龟
t.penup()
turtle.done()          # 一个海龟绘图程序的结束语句