from myclass.calculator import Calculator

c1 = Calculator(10, 4)

print(c1.add())
print(c1.sub())
print(c1.mul())
print(c1.div())

c2 = Calculator(23, 7)

print(c2.add())
print(c2.sub())
print(c2.mul())
print(c2.div())

print(Calculator(1, 2).add())