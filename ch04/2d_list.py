# 이차원 리스트의 생성과 출력

li = [
        [10,20],
        [30,40],
        [50,60]
    ]

print("li[0][0] =", li[0][0])
print("li[0][1] =", li[0][1])
print("li[1][0] =", li[1][0])
print("li[1][1] =", li[1][1])

print(len(li)) # 리스트의 크기 '행'
'''
for x, y in li:
    print(x, y)
'''

for i in range(len(li)):
    print(len(li[i]))
    for j in range(len(li[i])):
        print(li[i][j], end=' ')
    print()
               
