# 단위 변환 클래스

class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def convertor(self, val):
        return self.factor * val


if __name__ == "__main__":
    c1 = ScaleConverter("inches", "mm", 25)
    print("Converting 2 inches")
    print(str(c1.convertor(2)) + c1.units_to)