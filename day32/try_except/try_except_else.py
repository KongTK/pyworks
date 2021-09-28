# try ~ except ~ else
# 오류가 없을 때 try~else 실행
# 오류 있을 때 try~except 실행
# finally는 오류 여부와 상관 없이 항상 실행 - 외부장치를 초기화, 종료 시 주로 사용
try:
    print("1번")
    with open('animal.txt', 'r') as f:
        lines = f.readlines()
except:
    print("2번")
else:
    print("3번")
    for i in lines:
        print(i, end='')
        
finally:
    print("4번")
