# 웹 스크레이핑(크롤링)

from urllib import request

content = request.urlopen("http://daum.net")
print(content.read())