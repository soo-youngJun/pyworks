import random

# 주사위 10번
dice = []
for i in range(0, 10):
    n = random.randint(1, 6)
    dice.append(n)

#print(dice)

# 로또 번호 생성기
lotto =[]
'''
for i in range(0, 6):   # 중복되면 숫자가 부족할 수 있음
    n = random.randint(1, 45)
    if n not in lotto:   # 중복 방지
        lotto.append(n)
'''
while len(lotto) < 6:
    n = random.randint(1, 45)
    if n not in lotto:
        lotto.append(n)
        print(len(lotto), n)

print(lotto)
