# 변수 교환
blue = 1
red = 2
print("교환 전 : ")
print("blue =", blue, ", red =", red)

# 임시 변수 사용
""" yellow = blue
blue = red
red = yellow """
#한줄 주석은 #, 여러줄은 """ """로 지정

# 임시 변수 사용하지 않고 바로 교환(파이썬만 가능)
blue, red = red, blue

print("교환 후 : ")
print("blue =", blue, ", red =", red)
