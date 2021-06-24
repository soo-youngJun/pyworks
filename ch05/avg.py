# 리스트를 매개변수로 전달하기
# 점수의 평균 계산하기

def avg(a):
    sum = 0
    c = len(a)
    for i in a:
        sum += i
    return sum / c

kor = [70, 80, 60, 90, 100]
avge = avg(kor)
print("평균 점수 :", avge)

en = [55, 78, 99, 22, 34, 56, 88, 90]

print("평균 점수 :", avg(en))
