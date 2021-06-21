# 조건 : 현금이 있고, 카드가 있으면 택시를 타고, 아니면 걸어간다.

money = 3000
card = True
'''
if money > 4000 and card:
    print("택시를 탄다")
else:
    print("걸어간다")
'''
if money > 4000 or not card:
    print("택시를 탄다")
else:
    print("걸어간다")

# 조건 : 주머니에 현금이 있으면 택시를 타고, 아니면 걸어간다.

pocket = ['paper', '스마트폰', 'coin']
if 'money' in pocket:
    print('택시를 탄다')
else:
    print('걸어간다')
