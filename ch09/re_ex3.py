import re
# 태그 추출 - 점(.) 임의의 문자 1개, * 0개 이상 반복
str = "abcd<hr>Thank you"

#pat = re.compile("<(.*)>")  # 태그 제외하고 괄호 안의 내용
pat = re.compile("(<.*>)")   # 태그를 포함한 내용
m = re.findall(pat, str)
print(m)