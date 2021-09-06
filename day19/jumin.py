# 3
pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)
print()

# 4
pin = "881120-1068234"
print(pin[7])
if pin[7] == '1' or pin[7] == '3':
    print("남자")
else:
    print("여자")
print()

# 5
a = "a:b:c:d"
b = a.replace(':', '#')
print(b)
print()

# 6
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)
print()

# 7 리스트 -> 문자열
a = ['Life', 'is', 'too', 'short']
result = " ".join(a)
print(result)
