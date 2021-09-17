# find() 함수 - 문자열을 찾는 함수
# 인덱스 반환

str = "Hello"
x = str.find('H')
print(x) # 0 - H가 0번째 위치에 존재하기 때문

x = str.find('ll')
print(x)

x = str.find('m')
print(x)

if x >= 0:
    print("찾음")
else:
    print("찾는 문자가 없음")