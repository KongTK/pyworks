# 문자열 함수

print("split() 함수 - 구분자(구분기호-공백, ',', ':')")
s1 = "banana grape peach" # split을 붙이기 때문에 banana, X banana O
s1 = s1.split(' ') #공백으로 구분되어 리스트 형태로 반환
print(s1)
print(s1[0]) # print(s1[n:m])으로 문자 반환해야하는 것을 ','사용으로 간단히
print()

print("replace() 함수")
s2 = "Hello, World"
s2 = s2.replace("World", "Korea")
print(s2)
print()

print("format() 함수")
s3 = 'My name is {0}. I am {1} years old'.format('Mario', 40)
print(s3)
print()

print("I eat {0} apples".format(3))
n=3
print("I eat {0} apples".format(n))
day = 5
print("I eat {0} apples. so I was sick for {1} days".format(n, day))
