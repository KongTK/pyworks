# 반복문 : continue문

# 1 ~ 10 중 5만 제외 출력
for i in range(1, 11):
    if i == 5:
        continue # if 조건 달성시 for문 초기로 돌아가 계속(continue) 
    print(i)
print()

# 1 ~ 10 중 짝수 출력
for i in range(1, 11):
    if i % 2 == 1:
        continue 
    print(i)
