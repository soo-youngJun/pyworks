import re

str = "park 010-1234-5678"
#p = re.compile("(?P<name>\w+)\s+(?P<phone>\d+[-]\d+[-]\d+)")
#m = re.search(p, str)
#print(m.group(0))   # 전체 문자열
#print(m.group(1))
#print(m.group(2))

# sub 매서드 사용
#s = p.sub("\g<name> \g<phone>", str)  # 이름을 사용
p = re.compile("(\w+)\s+(\d+[-]\d+[-]\d+)")
s = p.sub("\g<2> \g<1>", str)  # 참조 번호를 사용
print(s)