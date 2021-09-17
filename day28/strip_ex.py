# strip() - 공백문자 제거
# lstrip() - 왼쪽 공백 문자 제거, rstrip() - 오른쪽 공백 제거

s1 = "    Hi, soo!"
print(s1.lstrip())

s2 = "Hi, soo!    "
print(s2.rstrip())

s3 = "Hi, soo!   "
print(s3.strip())

txt = "      banana     "
x = txt.strip()
print("Of all fruits", x, "is my favorite")