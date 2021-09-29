# 이름과 전화번호를 분리해서 추출하기
# sub(\g<그룹이름>)

import re
str = "jang 010-1234-5678"
# p = re.compile("(\w+)\s(\d+[-]\d+[-]\d+)") # \w = [0-9A-Za-z]
p = re.compile("(?P<name>\w+)\s+(?P<phone>[0-9]+[-]\d{4}[-]\d{4})")
s = p.sub("\g<name> \g<phone>", str)
print(s)
