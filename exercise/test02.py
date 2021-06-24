# p.112
# 1번

ko = 80
en = 75
ma = 55

sum = ko + en + ma
aver = sum / 3

print("홍길동 씨의 평균 점수는 ", aver, "점입니다")

# 2번

print(13 % 2) # 나머지가 0 이면 짝수, 1이면 홀수

num = 13

if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 3번

pin = "881120-1068234"
yyyymmdd = "19" + pin[:6]
num = pin[7:]

print(yyyymmdd)
print(num)

# 4번

gender = int(pin[7])

#print(gender)

if gender == 1:
    print("남성입니다.")
else:
    print("여성입니다.")


# 5번

a = "a:b:c:d"
b = a.replace(":", "#")
print(b)

# 6번

d = [1, 3, 5, 4, 2]
d.sort()
d.reverse()
print(d)

# 7번

e = ['Life', 'is', 'too', 'short']
result = " ".join(e)
print(result)

# split 예제

'''
msg = s.split()
print(msg)
'''
s = "a:b:c:d"
s = s.split(':')
print(s)

# 8번

a = (1, 2, 3)
a = a + (4, )
print(a)

# 9번

a = dict()
a['name'] = 'python'
print(a)
a[('a',)] = 'python' # key -> 튜플
print(a)
a[250] = 'python'
print(a)

# 10번

a = {'A':90, 'B':80, 'C':70}
result = a['B']
print(a)
print(result)

# 11번

a = [1,1,1,2,2,3,3,3,3,4,4,5]
aSet = set(a) # 중복 제거
b = list(aSet) # list형으로 변환

print(b)

# 12번

a = b = [1,2,3]
a[1] = 4
print(b)

