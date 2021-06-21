# 놀이공원 입장료 계산

age = int(input("나이를 입력해주세요: "))
charge = 0 # 전역변수가 없어도 실행가능

if age < 8:
    print("취학전 아동입니다.")
    charge = 1000
elif age <14: # age >=8 and age <14
    print("초등학생입니다.")
    charge = 2000
elif age <20: # age >=14 and age <20
    print("중,고등학생입니다.")
    charge = 2500
else:
    print("일반인 입니다.")
    charge = 3000
    
print("입장료는 %d원입니다." % charge)
