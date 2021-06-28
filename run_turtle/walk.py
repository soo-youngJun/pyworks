# 랜덤하게 거북이가 걸어가기

import turtle as t
import random as r

t.shape('turtle')
t.speed(5)
t.bgcolor('pink')
t.setup(400,400) # 작업영역 크기

for x in range(100): # 거북이가 100번 움직임
    angle = r.randint(1, 360) 
    t.setheading(angle) # 거북이의 방향
    t.forward(15) 

t.mainloop()