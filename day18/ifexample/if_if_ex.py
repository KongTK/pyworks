# 중첩 if
# 조건 : 10을 기준으로 큰 수와 작은 수 구분하고 홀, 짝도 구분

n = 4
if n > 10:
    if n % 2 == 0:
        print("10보다 큰 짝수입니다")
    else:
        print("10보다 큰 홀수입니다")
else:
    if n % 2 == 0:
        print("10 이하의 짝수입니다")
    else:
        print("10 이하의 홀수입니다")

# if ~ elif ~ else 구현하기
if n > 10 and n % 2 == 0:
    print("10보다 큰 짝수입니다")
elif n > 10 and n % 2 == 1:
    print("10보다 큰 홀수입니다")
elif n <= 10 and n % 2 == 0:
    print("10 이하의 짝수입니다")
elif n <= 10 and n % 2 == 1:
    print("10 이하의 홀수입니다")
