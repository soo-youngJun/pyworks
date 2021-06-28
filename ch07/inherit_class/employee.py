from person import Person
# 멤버 매개변수가 있는 상속

class Employee(Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)  # 부모 멤버는 super()를 사용
        self.id = id

        def getname(self):
            return self.name

        def getage(self):
            return self.age

        def getempid(self):
            return self.empid

e1 = Employee("북한강", 20, 201)
print("이름 : ", e1.getname())
print("나이 : ", e1.getage())
print("사번 : ", e1.getempid())

e2 = Employee("금강", 30, 202)
print(e2.name, e2.age, e2.empid)