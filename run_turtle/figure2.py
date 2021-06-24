# 도형 그리기 (반복문)

import turtle as t

t.shape('turtle')

# 사각형 그리기
n = 8
for i in range(n):
    t.forward(100)
    t.right(360 / n)


# 삼각형 그리기
t.color('red')
t.pensize(2)
for i in range(0, 3):
    t.forward(100)
    t.left(120)


# 원 그리기
t.color('blue')
t.pensize(3)
t.circle(50)

