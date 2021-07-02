# 1번
'''
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val
        return self.value

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
        return self.value
# 2번
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
        return self.value
# 부모 클래스의 인스턴스
c = Calculator()
print(c.add(10))
print(c.value)

cal = UpgradeCalculator()
print(cal.add(10))
print(cal.minus(7))
print(cal.value)

cal = MaxLimitCalculator()
print(cal.add(50))
print(cal.add(60))
print(cal.value


# 3번

all([1, 2, abs(-3)-3]) # False
chr(ord('a'))=='a' # True



# 4번

li = [1, -2, 3, -5, 8, -3]

#print(list(filter(lambda x : x >= 0, li)))
def positive(a):
    a2 = []
    for i in li:
        if i >= 0:
            a2.append(i)
    return a2

li2 = positive(li)
print(li2)
'''

# 6번
def times(a):
    a2 = []
    for i in a:
        a2.append(i*3)
    return a2

li = [1, 2, 3, 4]
li2 = times(li)
print(li2)

print(list(map(lambda x: x * 3, li)))