from turtle import *

# 副程式：提起筆移動到(x,y)再放下筆
def go_to(x, y):
    penup()
    goto(x, y)
    pendown()

# =======
# 程式開始
# =======
screensize(800, 600)    # 設定畫布大小
title('皮卡丘')          # 視窗抬頭
pensize(3)              # 設定畫筆粗細為3
speed(0)                # 畫圖速度

# 開始畫身體
fillcolor('#F6D02F')
begin_fill()
# 右臉輪廓
penup()
circle(130, 40)
pendown()
circle(100, 105)
left(180)
circle(-100, 5)

# 右耳朵
seth(20)
circle(300, 30)
circle(30, 50)
seth(190)
circle(300, 36)

# 上輪廓
seth(150)
circle(150, 70)

# 左耳朵
seth(200)
circle(300, 40)
circle(30, 50)
seth(20)
circle(300, 35)

# 左臉輪廓
seth(240)
circle(105, 95)
left(180)
circle(-105, 5)

# 左手
seth(210)
circle(500, 18)
seth(200)
fd(10)
seth(280)
fd(7)
seth(210)
fd(10)
seth(300)
circle(10, 80)
seth(220)
fd(10)
seth(300)
circle(10, 80)
seth(240)
fd(12)
seth(0)
fd(13)
seth(240)
circle(10, 70)
seth(10)
circle(10, 70)
seth(10)
circle(300, 18)

seth(75)
circle(500, 8)
left(180)
circle(-500, 15)
seth(250)
circle(100, 65)

# 左腳
seth(320)
circle(100, 5)
left(180)
circle(-100, 5)
seth(220)
circle(200, 20)
circle(20, 70)

seth(60)
circle(-100, 20)
left(180)
circle(100, 20)
seth(300)
circle(10, 70)

seth(60)
circle(-100, 20)
left(180)
circle(100, 20)
seth(10)
circle(100, 60)

# 橫向
seth(180)
circle(-100, 10)
left(180)
circle(100, 10)
seth(5)
circle(100, 10)
circle(-100, 40)
circle(100, 35)
left(180)
circle(-100, 10)

# 右腳
seth(290)
circle(100, 55)
circle(10, 50)

seth(120)
circle(100, 20)
left(180)
circle(-100, 20)

seth(0)
circle(10, 50)

seth(110)
circle(100, 20)
left(180)
circle(-100, 20)

seth(30)
circle(20, 50)

seth(100)
circle(100, 40)

# 右側身體輪廓
seth(200)
circle(-100, 5)
left(180)
circle(100, 5)
left(30)
circle(100, 75)
right(15)
circle(-300, 21)
left(180)
circle(300, 3)

# 右手
seth(43)
circle(200, 60)

right(10)
fd(10)

circle(5, 160)
seth(90)
circle(5, 160)
seth(90)

fd(10)
seth(90)
circle(5, 180)
fd(10)

left(200)
fd(10)
circle(5, 170)
fd(10)
seth(240)
circle(50, 30)
end_fill()

# 手指
go_to(130, 125)
seth(-20)
fd(5)
circle(-5, 160)
fd(5)
go_to(166, 130)
seth(-90)
fd(3)
circle(-4, 180)
fd(3)
seth(-90)
fd(3)
circle(-4, 180)
fd(3)

# 尾巴
go_to(168, 134)
fillcolor('#F6D02F')
begin_fill()
seth(40)
fd(200)
seth(-80)
fd(150)
seth(210)
fd(150)
left(90)
fd(100)
right(95)
fd(100)
left(110)
fd(70)
right(110)
fd(80)
left(110)
fd(30)
right(110)
fd(32)

right(106)
circle(100, 25)
right(15)
circle(-300, 2)

seth(30)
fd(40)
left(100)
fd(70)
right(100)
fd(80)
left(100)
fd(46)
seth(66)
circle(200, 38)
right(10)
fd(10)
end_fill()

# 尾巴花紋 
go_to(126.82, -156.84)
fillcolor('#923E24')
begin_fill()
seth(30)
fd(40)
left(100)
fd(40)
pencolor('#923e24')
seth(-30)
fd(30)
left(140)
fd(20)
right(150)
fd(20)
left(150)
fd(20)
right(150)
fd(20)
left(130)
fd(18)
pencolor('#000000')
seth(-45)
fd(67)
right(110)
fd(80)
left(110)
fd(30)
right(110)
fd(32)
right(106)
circle(100, 25)
right(15)
circle(-300, 2)
end_fill()

# 帽子
go_to(-134, 148)
fillcolor('#CD0000')
begin_fill()
seth(200)
circle(400, 7)
left(180)
circle(-400, 30)
circle(30, 60)
fd(50)
circle(30, 45)
fd(60)
left(5)
circle(30, 70)
right(20)
circle(200, 70)
circle(30, 60)
fd(70)
right(35)
fd(50)
circle(8, 100)
end_fill()

go_to(-168, 185)
seth(36)
circle(-270, 54)
left(180)
circle(270, 27)
circle(-80, 98)

fillcolor('#444444')
begin_fill()
left(180)
circle(80, 197)
left(58)
circle(200, 45)
end_fill()

go_to(-58, 270)
pencolor('#228B22')
dot(35)

go_to(-30, 280)
fillcolor('#228B22')
begin_fill()
seth(100)
circle(30, 180)
seth(190)
fd(15)
seth(100)
circle(-45, 180)
right(90)
fd(15)
end_fill()
pencolor('#000000')

# 下嘴唇
go_to(-5, 25)
fillcolor('#88141D')
begin_fill()

# 左邊
seth(190)
l1 = [] # 用來記錄下嘴唇的座標，等一下畫舌頭時要用
a = 0.7
for i in range(28):
    a += 0.1
    right(3)
    fd(a)
    l1.append(pos())
go_to(-5, 25)

# 右邊
seth(10)
l2 = []
a = 0.7
for i in range(28):
    a += 0.1
    left(3)
    fd(a)
    l2.append(pos())

# 上嘴唇
seth(10)
circle(50, 15)
left(180)
circle(-50, 15)
circle(-50, 40)
# 右邊
seth(233)
circle(-50, 55)
left(180)
circle(50, 12.1)
end_fill()

# 舌頭
go_to(17, 54)
fillcolor('#DD716F')
begin_fill()
seth(145)
circle(40, 86)
# 走一圈包圍起來才會填滿
penup()
for (x,y) in reversed(l1[:20]):
    goto(x, y+1.5)
for (x,y) in l2[:20]:
    goto(x, y+1.5)
pendown()
end_fill()

# 鼻子
go_to(-17, 94)
seth(8)
fd(4)
back(8)

# 左臉頰楕圓
tracer(False) # 不顯示動畫
go_to(-126, 32)
seth(300)
fillcolor('#DD4D28')
begin_fill()
a = 2.3
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a -= 0.05
    else:
        a += 0.05
    left(3)
    fd(a)
end_fill()

# 右臉頰楕圓
go_to(107, 63)
seth(60)
fillcolor('#DD4D28')
begin_fill()
a = 2.3
for i in range(120):
    if 0 <= i < 30 or 60 <= i < 90:
        a -= 0.05
    else:
        a += 0.05
    lt(3)
    fd(a)
end_fill()
tracer(True) # 恢復動畫

# 左耳朵
go_to(-250, 100)
fillcolor('#000000')
begin_fill()
seth(330)
circle(100, 35)
seth(219)
circle(-300, 19)
seth(110)
circle(-30, 50)
circle(-300, 10)
end_fill()

# 右耳朵
go_to(140, 270)
fillcolor('#000000')
begin_fill()
seth(300)
circle(-100, 30)
seth(35)
circle(300, 15)
circle(30, 50)
seth(190)
circle(300, 17)
end_fill()

# 左眼
go_to(-85, 90)
seth(0)
fillcolor('#333333')
begin_fill()
circle(22)
end_fill()

go_to(-85, 100)
fillcolor('#000000')
begin_fill()
circle(10)
end_fill()

go_to(-79, 112)
fillcolor('#ffffff')
begin_fill()
circle(10)
end_fill()

# 右眼
go_to(50, 110)
seth(0)
fillcolor('#333333')
begin_fill()
circle(22)
end_fill()

go_to(50, 120)
fillcolor('#000000')
begin_fill()
circle(10)
end_fill()

go_to(44, 132)
fillcolor('#ffffff')
begin_fill()
circle(10)
end_fill()

# 顯示班級座號姓名
go_to(0, -200)
pencolor("purple")
write("11604 李芯柔", align='center', font=('微軟正黑體', 24, 'bold'))

hideturtle()
mainloop()
