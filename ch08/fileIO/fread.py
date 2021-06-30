try:
    f = open('c:/pyfile/hello.txt', 'r')
    date = f.read()
    print(date)
    f.close()
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")