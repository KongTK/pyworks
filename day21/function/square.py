
# 제곱수 계산하는 함수 정의
import math

def square(x):
    return x * x

# 거듭제곱 계산하는 함수
# 거듭제곱 x ** n = x^n
def double_times(x, y):
    return x ** y

# 절대값 함수
def abs_v(x):
    if x < 0:
        return -x
    else:
        return x

# 절대값 함수 2
def abs_v2(x):
    y = x * x
    return math.sqrt(y)

n = square(3)
n2 = double_times(2, 3)
print("제곱수 :", n)
print("거듭제곱 수 :", n2)
print("절대값 :", abs_v(-10))
print("절대값 :", abs_v2(-10))