# set 자료 구조
# 순서가 없고 중복이 불가

s = {2, 4, 6, 8}
print(s)

# 요소 추가 - add()
s.add(10)
s.add(4) # 중복이라 추가 안됨
print(s)

# 요소 삭제 - remove()
s.remove(8)
print(s)

str = set("Hello")
print(str)

name = set(['콩쥐', '팥쥐', '콩쥐'])
print(name)