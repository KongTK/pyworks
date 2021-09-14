# 1차원 리스트
d1 = [10, 20, 30]
print(d1)
for i in d1:
    print(i)

# 추가
d1.append(40)
print(d1)

# 20 삭제
d1.remove(20)
print(d1)
print(len(d1))

sum_v = 0
for i in d1:
    sum_v += i
avg = sum_v / len(d1)
print("합계 :", sum_v)
print("평균 : %.2f" % avg)

'''
# 2차원 리스트 - 리스트 내부에 리스트 존재
d2 = [[10, 20], [30, 40]]
print(d2[0][0])
print(d2[0][1])
print(d2[1][0])
print(d2[1][1])

for x, y in d2:
    print(x, y)
'''