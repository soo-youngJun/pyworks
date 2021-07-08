import re

# 그룹핑된 문자열에 이름 붙이기
# ?P<그룹이름>
p = re.compile("(?P<name>\w+)\s(?P<phone>\d{3}[-]\d+[-]\d+)")
s = p.search("jang 010-1234-5678")
print(s.group(1))
print(s.group(2))
print(s.group("name"))
print(s.group("phone"))
