# 가변 매개변수 * 들어가면 튜플 자료구조
def animal(*args):
    print(args)

def avg(*args):
    sum = 0
    for i in args:
        sum += i
        print(i, sum)
    return sum / i

animal('cow')
animal('cow', 'pig')

# 평균 구하기
print(avg(1, 2, 3))
print(avg(1, 2, 3, 4))