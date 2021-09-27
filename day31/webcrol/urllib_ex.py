# 웹사이트 url에 접근
# request.urlopen()
from urllib import request

url = "http://www.naver.com"
html = request.urlopen(url) # html - 컨텐츠
print(html.read())

