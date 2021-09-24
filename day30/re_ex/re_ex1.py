# 정규 표현식
import re
# match()함수 -> find()와 유사
p = re.compile("[a-z]+") # []-매치되는 문자, []+ 1번이상 반복되는 문자
m = p.match('afternoon')
print(m)

# search()함수
s = p.search("2021 python")
print(s)

