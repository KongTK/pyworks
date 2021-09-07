# 함수 쓰지 않고

# 최대값 계산하기
v = [70, 80, 55, 60, 90]
max = v[0] # 최대값 아니지만 최대값으로 설정 후 비교
for i in v:
    if max < i:
        max = i
print("최대값 :", max)

# 최소값 계산하기
min = v[0]
for i in v:
    if min > i:
        min = i
print("최소값 :", min)
