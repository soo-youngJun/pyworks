# 전역변수의 범위

def price():
    price = 250 * quantity
    print(f"{quantity}개에 {price}원입니다.")

quantity = 2
price()
