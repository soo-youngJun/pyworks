# 정사각형의 넓이

size = int(input("한 변의 길이 : "))
area = size * size
print("정사각형의 넓이 : ",area)
print("정사각형의 넓이 : %dcm" % area)
# 대응출력방법 -> 정수 %d, 문자 %s, 소수 %f (%.2f 소숫점 2자리까지) 

# 삼각형의 넓이

width = int(input("밑 변의 길이 : "))
height = int(input("높이 : "))
area = width * height / 2
print("삼각형의 넓이 : %dcm " % area)
