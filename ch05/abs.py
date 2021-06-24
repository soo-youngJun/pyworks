# abs() 직접 정의
# 절대값 알고리즘1

import math # math 모듈 호출

def abs_sign(x):
    if x < 0:
        return -x # x * -1
    return x


# 절대값2
def abs_square(x):
    y = x * x
    return math.sqrt(y) # 루트

n1 = abs_sign(-3)
n2 = abs_square(-3)

print(n1)
print(n2)
