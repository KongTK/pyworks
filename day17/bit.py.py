# 10진수, 2진수, 16진수
num = 10
b_num = 0b1010 # 0b 부착시 2진수를 10진수로 전환
h_num = 0xA # 0x 부착시 16진수를 10진수로 전환

print("num =", num)
print("b_num =", b_num)
print("h_num =", h_num)

# 아스키 코드
print("코드 33 : ", chr(33))
print("코드 48 : ", chr(48))
print("코드 97 : ", chr(97))
print()

# 비트 이동 연산자(<< - 자리수 커짐, >> - 자리수 작아짐)
num1 = 5 # 00000101
print("num1 = ", num1)
print("num1 << 2 =", num1 << 2) # 00010100 -> 20
print("num1 >> 2 =", num1 >> 2) # 00000001 -> 1

# 비트 논리 연산자(&:논리곱(모두1일때 1), |(논리합(하나만 1이어도 1), ~(반전))
num1 = 8 #00001000
num2 = 9 #00001001
print("num1 = ", num1)
print("num2 = ", num2)
print("num1 & num2 : ", num1 & num2) #00001000
print("num1 | num2 : ", num1 | num2) #00001001
