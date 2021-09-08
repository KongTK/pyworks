# 절대값 계산하는 함수 정의
# 조건 - 음수는 양수로 변환, 양수는 그대로
def abs_v(x):
    if x < 0:
        return -x # x = -1*x 대신 return -x 해도됨
    else:
        return x # 굳이 x = x 안넣어도됨

print(abs_v(-3))    
print(abs_v(3))    
