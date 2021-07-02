# 영어 타자 연습 프로그램
import random
import time

f = open('words.txt', 'r')
word = f.read().split()   # 공백 또는 줄바꿈으로 나눔/ readline의 경우 1가지만 출력
print(word)
f.close()

n = 1   # 문제 번호
print("[타자 게임]준비되면 엔터")
input()
start = time.time()
q = random.choice(word)  # 단어 랜덤 선택
while n <= 10:
    print("문제", n)
    print(q)
    x = input()
    if q == x:
        print("통과!")
        n += 1  # 통과한 경우만 10번까지 실행
        q = random.choice(word)
    else:
        print("오타! 다시 도전")
    # n += 1 맞았는지 상관없이 10번만 실행

end = time.time()
et = end - start
print("타자 시간: %.2f초" % et)