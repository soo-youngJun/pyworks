# try~except~finally

def divide(x, y):
    try:
        div = x / y
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    else:
        print(div)
    finally:
        print("여기는 꼭 수행하는 구간입니다.")  # 보통 f.close, reset code 등..


divide(3, 0)