# 파일 열기(open()) -> 파일 쓰기(write()) -> 파일 닫기(close())

f = open('C:/pyfile/hello.txt', 'w')

f.write('Hello~ python\n')
#f.write(1000) 숫자만 입력불가 - 포맷 방식으로 입력 가능
#f.write('%d\n' % 100) # 숫자 입력, \n 한줄띄기
num = "%.1f\n" % 7.3 # 소수 입력
f.write(num) # 변수에 담아서 숫자 입력
f.write('안녕~ 파이썬\n')
f.close()