# list의 최대값과 최소값, 정렬

score = [70, 80, 50, 60, 90, 45]
max = score[0]
min = score[0]
n = len(score)

for i in range(1, n):
    if max < score[i]:
        max = score[i]

print("최고 점수 %d점" % max)

for i in range(1, n):
    if min > score[i]:
        min = score[i]

print("최소 점수 %d점" % min)


# 오름차순 정렬 (score.sort()) 

for i in range(0, n):
    for j in range(0, n-1):
        if score[j] > score[j+1]: # 반대로 하면 내림차순
            score[j], score[j+1] = score[j+1], score[j]
'''
 1행 70 50 60 80 45 90
 2행 50 60 70 45 80 90
 3행 50 60 45 70 80 90
 4행 50 45 60 70 80 90
 5행 45 50 60 70 80 90
'''

for i in score:
    print(i, end=' ')
