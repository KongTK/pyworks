import re

str = "123?45yy7890 hi 999 hello"
pat = re.compile("\d{1,3}") # \d:0~9, {최소, 최대}
m = re.findall(pat, str)
print(m)

m2 = re.findall('[A-z]+', str)
print(m2)

m3 = re.findall('[1-5]{1,2}', str) # [1-5]이므로 7~0 반환 X
print(m3)

m4 = re.findall('[^\s\w]+', str) # \s 공백문자 \w 모든문자([0-9][a-z][A-Z])
print(m4)