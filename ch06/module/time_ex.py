import time

print(time.time()) # 1970.1.1 자정 이후를 초로 환산

today = time.time() / 60 / 60 / 24

print(time.localtime())
print(time.ctime()) # 날짜와 시간 요일 표시
print(time.strftime('%x', time.localtime())) # 06/23/21
print(time.strftime('%c', time.localtime(time.time())))

# time.sleep(1) : 1초간 대기 (python만 1초를 1로 표기)

for i in range(1, 11):
    print(i)
    time.sleep(1)
    
