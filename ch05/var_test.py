# 전역변수와 지역변수

a = 1

def vartest(a):
    a = a + 1
    return a

print(vartest(a))
print(a)
