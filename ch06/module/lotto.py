# 로또 번호 생성 - 중복되지 않는 번호로 구성

import random as r

lotto = []

for x in range(6): # 랜덤 횟수 6회
    n = r.randint(1, 45)
    if n not in lotto:
        lotto.append(n)
    #if len(lotto) == 6:
        #break
print(lotto)

lotto2 = []

while len(lotto2) < 6: # 번호가 6개 될 때까지 반복
    n = r.randint(1, 45)
    if n not in lotto2:
        lotto2.append(n)
print(lotto2)
    
