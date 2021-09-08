# 지역 변수 사용하기

def one_up():
    x = 1 # 지역변수 : 호출할때마다 초기화
    x += 1
    return x

print(one_up())
print(one_up())
print(one_up())
# 지역변수는 매번 초기화되어 2 반복, 전역변수는 프로그램 종료까지 남아 2,3,4 순차 증가
