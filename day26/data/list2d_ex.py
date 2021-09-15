# 2차원 리스트 연산
d2 = [[80], [90], [100]] # 3행 1열

# 리스트 추가
d2.append([70])
print(d2)

# 합계 리스트 추가
sum_v = 0
n = len(d2)
for i in range(0, n):
    sum_v += d2[i][0]
    print('sum_v=', sum_v, 'd2[i][0]=', d2[i][0])

avg = sum_v / n
d2.append([sum_v])
d2.append(avg)
print("국어 점수의 평균 : %.1f" % avg)
print(d2)