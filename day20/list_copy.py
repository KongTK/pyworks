# 리스트 복사
li = [5, 7, 3, 2, 9]
li2 = [] # 빈 리스트 생성
li3 = [] # li2

for i in li:
    li2.append(i)
print(li2) # 리스트 형태로 출력

for i in li2:
    print(i) # 전체 요소(값) 출력

# 짝수만 저장
for i in li:
    if i % 2 == 0:
        li3.append(i)
print(li3)
