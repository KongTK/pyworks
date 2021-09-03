# 중첩 for 문

for i in range(0, 5):
    for j in range(0, 5):
        print('가', end=' ')
    print()

for i in range(0, 5):
    for j in range(1, 6):
        num = i*5+j
        print(num, end=' ')
    print()

