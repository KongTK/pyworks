# findall()함수 - 내용을 리스트로 반환
import re

str = "Two is too"
m1 = re.findall("T[ow]o", str) # 대문자 T이기 때문에 too는 반환 X
print(m1)

m2 = re.findall("T[ow]o", str, re.IGNORECASE) # IGNORECASE 대소문자 허용
print(m2)

pat = re.compile("T[w]o")
m3 = re.findall(pat, str)
print(m3)