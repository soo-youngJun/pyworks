from person import Person

class Student(Person):
    def __init__(self, name, age, stuid):
        super().__init__(name, age)
        self.stuid = stuid

    def showinfo(self):
        print(self.name, self.age, self.stuid)

s1 = Student('이강', 19, 101)
s1.showinfo()
s2 = Student('해찬들', 17, 102)
s2.showinfo()