# 매개변수가 1개인 lambda 함수

def times(x):
    return x * 3

def square(y):
    return y * y

result = times(5)
print(result)
print(square(2))

print("lambda로 구현")
times2 = lambda x : x * 3
print(times(5))
print((lambda x : x * 3)(4))

square2 = lambda x : x*x
print(square2(2))
print((lambda x : x * x)(2))