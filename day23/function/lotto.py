import random as r

# 로또 : 1~45 수가 6개
lotto = []
'''
for i in range(6):
    rnd = r.randint(1, 45)
    if rnd not in lotto:
        lotto.append(rnd)
로또는 중복되면 안 되는데 for로 중복제거하면 6개에서 중복만큼 빠져서 부족
따라서 for 대신 while 사용
'''

while len(lotto) < 6:
    rnd = r.randint(1, 45)
    if rnd not in lotto:
        lotto.append(rnd)
print(lotto)