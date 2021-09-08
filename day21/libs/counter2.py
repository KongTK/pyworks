# 1씩 증가하는 Counter 클래스 정의
class Counter:
    x = 0  # 클래스 변수 : 전역 변수와 유사 개념, 인스턴스 변수(지역 변수와 유사 개념)
    
    def __init__(self):
        Counter.x += 1

    def __str__(self):
        return self.x

c1 = Counter()
print(c1.x)

c2 = Counter()
print(c2.x)

c3 = Counter()
print(c3.x)

