# 절대값 계산하는 함수 정의
# 조건 - 음수는 양수로 변환, 양수는 그대로
def abs_v(x):
    if x < 0:
        x = -1*x
    else:
        x = x
    return x

print(abs_v(-3))    
