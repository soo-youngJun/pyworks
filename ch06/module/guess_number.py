# 1 ~30까지 숫자 추측 게임

import random as r

com = r.randint(1, 30)

while True:
    try:
        guess = int(input("맞혀보세요(1~30) : "))
        #if guess > 30 or guess < 1:
        #    print("유효한 숫자 범위가 아닙니다.")
        #elif guess == com:
        #    print("정답!!")
        #    break
        if guess == com:
            print("정답!!")
            break
        elif guess > com and guess < 31:
            print("너무 커요!!")
        elif guess > 30 or guess < 1:
            print("유효한 숫자 범위가 아닙니다.")
        else:
            print("너무 작아요!!")
    except ValueError:
        print("숫자가 아닙니다. 다시 입력해주세요.")
        
