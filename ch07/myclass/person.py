# Person 클래스 생성과 사용

class Person:
    def __init__(self):  # 초기자(생성자 함수)
        self.__name = '강하늘'
        self.age = 30

    def getname(self):  # 멤버 변수에 직접 접근하지 않도록 get()을 사용
        return self.name

    def getage(self):
        return self.age


p = Person()  # 객체변수(instance)
#p.__name = '박바다'
#print(p.__name, p.age)
print(p.getname())
print(p.getage())