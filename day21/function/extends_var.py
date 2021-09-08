# 가변 매개 변수 : 정해지지 않은 매개 변수

# 문자열이 추가되는 함수
def merge_text(*text): # * 정해지지 않음
    result = "" #빈 문자 선언(초기화)
    for t in text:
        result = result + t
    return result # for 안에서 return하면 안 됨

# 숫자를 더한 후 평균을 계산
def calc_avg(*x):
    total = 0
    for i in x:
        total += i
    avg = total / len(x)
    return avg

if __name__ == "__main__": # 외부 호출시에는 포함되지 않도록
    # 문자열 더하기
    text1 = merge_text("코스모스")
    text2 = merge_text("코스모스 ", "국화")
    print(text1)
    print(text2)

    # 평균 계산
    n1 = calc_avg(1, 2)
    n2 = calc_avg(1, 2, 3, 4)
    print(n1)
    print(n2)