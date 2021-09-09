# list 예제
# li2에 li 요소에 3을 곱하여 저장
li = [1, 2, 3, 4]
li2 = []

for i in li:
    i = i*3
    li2.append(i) # li2.append(i*3)이 더 깔끔
print(li2)

# 합계와 평균
total = 0
avg = 0
for i in li:
    total += i
avg = total / len(li)

print("개수 :", len(li))
print("합계 :", total)
print("평균 :", avg)
