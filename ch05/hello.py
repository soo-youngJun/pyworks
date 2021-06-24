# 함수의 정의 및 호출
# return이 없고 매개변수 없는 함수

def say():
    print("안녕하세요")

# return이 없고 매개변수 있는 함수

def say2(name):
    #print(f"{name}님 반갑습니다.")
    print("{}님 반갑습니다.".format(name))
    

say() # 호출
say() 
print("="*30)
say2('김대한')
say2('SY')
