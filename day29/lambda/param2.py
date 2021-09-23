# 매개변수가 2개인 람다 함수

def calc(x, y): # 거듭제곱 계산
    return x ** y

print(calc(2, 3)) # 8

print("== lambda 함수로 구현 ==")
calc2 = lambda x, y : x + y
print(calc2(2, 3))
print((lambda x,y:x**y)(2,3))