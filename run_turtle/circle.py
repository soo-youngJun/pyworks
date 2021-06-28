# 여러 개의 원 만들기

import turtle as t

t.speed(0) # 1~9, 0이 가장 빠름
t.color('green')
t.bgcolor('gray')

n = 50
for x in range(n):
    t.circle(80)
    t.left(360/n)

t.mainloop()