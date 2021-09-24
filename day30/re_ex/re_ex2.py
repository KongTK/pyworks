# '*'와 '+' 차이
# * 문자가 0번 이상 반복
# + 문자가 1번 이상 반복
import re
p1 = re.compile("ca*t") # 정규식

m1 = re.findall(p1, "caat")
print(m1)

m2 = re.findall(p1, "ct")
print(m2)

p2 = re.compile("ca+t")
m1 = re.findall(p2, "caat")
print(m1)

m2 = re.findall(p2, "ct")
print(m2)