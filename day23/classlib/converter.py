# 단위 변환 클래스 만들기

class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def convert(self, val):
        return self.factor * val

c1 = ScaleConverter("inch", 'mm', 25.4) # 1inch = 2.54cm = 25.4mm
print("== " + c1.units_from + "을 " + c1.units_to + "로 변환 ==")
print("1인치는 " + str(c1.convert(3)) + c1.units_to)

c2 = ScaleConverter("KB", "Byte", 1024)
print("== " + c2.units_from + "을 " + c2.units_to + "로 변환 ==")
print("1KB는 " + str(c2.convert(3)) + c2.units_to)
