# 온도 변환기 클래스

class Converters:
    def __init__(self, unit_from, unit_to, factor, offset):
        self.unit_from = unit_from  # 바꿀 온도
        self.unit_to = unit_to   # 결과 온도
        self.factor = factor   # 요소
        self.offset = offset   # 요소2

    def convert(self, value):
        return value * self.factor + self.offset


if __name__ == "__main__":
    conv = Converters('C', 'F', 1.8, 32)
    print(str(conv.convert(23)) + conv.unit_to)