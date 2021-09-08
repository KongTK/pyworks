class Counter:
    def __init__(self):
        self.x = 0
        self.x += 1
    def __str__(self):
        return self.x

c1 = Counter()
print(c1.x)

c2 = Counter()
print(c2.x)

# 초기로 돌아가서 n번 반복하여도 결과는 전부 1