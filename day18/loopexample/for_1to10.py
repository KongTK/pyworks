# for문 사용하기
# range(시작, 끝, 증감수치)

# 1 ~ 11 출력
for i in range(1, 11, 1):
    print(i, end = " ")
    # end하지 않고 " " 옆으로 공백 추가 = 가로로 나열 
print()

# 0 ~ 9 출력
for i in range(10): # 초기값 설정을 하지 않으면 0부터 시작
    print(i, end = " ") 
print()

# 1 ~ 10 중 홀수 출력
for i in range(1, 11, 2):
    print(i, end = " ")
print()

for i in range(1, 11, 1):
    if i % 2 == 1:
        print(i, end = " ")
