# 정규 표현식 예제

import re

#p = re.compile('[a-z]+')  # + 는 앞문자가 1개 이상 반복을 의미하는 메타 문자
p = re.compile('a.b')  # . 은 임의의 문자 1개 메타 문자

m = p.match('afternoon')   # match()는 처음부터 문자를 검색 =find()와 비슷
print(m)                   #findall() 전체를 검색해서 리스트로 반화 =findall()
print(m.group())  # group()은 문자열을 표시해주는 함수

