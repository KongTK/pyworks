# 자리 배치도 프로그램

x = input("입장객 수 : ")
customer = int(x)
y = input("열 수 : ")
col_num = int(y)

# 나누어 떨어지는 경우, 그렇지 않은 경우
if customer % col_num == 0:
    row_num = int(customer / col_num)
else:
    row_num = int(customer / col_num) + 1

#print(str(row_num) + "개의 줄이 필요합니다.")

for i in range(0, row_num):   # 행, 줄
    for j in range(1, col_num+1):  # 열
        seat_num = i*col_num+j
        if seat_num > customer:
            break
        print("좌석" + str(seat_num), end=' ')
    print()
