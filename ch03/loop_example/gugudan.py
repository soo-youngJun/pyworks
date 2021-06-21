# 구구단 출력
# 단 입력
dan =int(input("단 입력: "))
for i in range(1, 10):
    print("%d x %d = %d" % (dan, i, dan*i))
    
# 1~9단 출력
for i in range(1, 10):
    for j in range(1, 10):
        print("%d x %d = %d" % (i, j, i*j))
    print('')
