# raise : 에러 미뤄둔다. 사용하는 쪽에서 발생하도록 함

class Bird:
    def fly(self):
        #print("새가 하늘을 높이 납니다.")
        raise NotImplemented

class Eagle(Bird):
    #pass
    def fly(self):
        print("독수리가 하늘을 높이 납니다.")

eagle = Eagle()
eagle.fly()