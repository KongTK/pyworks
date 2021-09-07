# return이 있는 함수

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

total = add(10, 11) # add 함수 호출
minus = sub(10, 11) # sub 함수 호출
print("두 수의 합 = {0}".format(total))
# print(x) 에러 발생 : x가 지역 변수여서 add 후 소멸
print("두 수의 차 = {0}".format(minus))
