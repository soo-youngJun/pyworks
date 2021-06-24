# set() 자료구조의 특징
# 순서가 없고, 중복이 허용되지 않음

s = set()
s.add(1)
s.add(2)
print(s)

# 중복 저장이 안됨
s2 = set(['cow', 'cat', 'dog', 'dog'])
print(s2)

# 리스트와 비교
ani = ['cow', 'cat', 'dog', 'dog']
print(ani)
