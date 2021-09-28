# 예외 만들기 - 사용자가 직접 만들기
# 내장 exception 클래스를 상속하여 만듬

class MyError(Exception):
    # pass
    def __str__(self):
        return "허용되지 않는 별명입니다"

def say_nick(nick):
    if nick == '바보':
        raise MyError() # 오류는 없지만 비속어 사용 등을 막기 위해 사용자가 임의로 에러로 지정
    print(nick)

# Error를 사용하는 곳에서 try~except 처리해야 함
try:
    say_nick('Hero')
    say_nick('angel')
    say_nick('바보')
except MyError as e: # e = exception 약자
    # print("허용되지 않는 별명입니다")
    print(e)
