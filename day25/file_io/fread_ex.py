# with ~ as 읽어오기
# kbo2021.txt

try:
    with open("C:/pyfile/kbo2021.txt", 'r') as f:
        # data = f.read()
        while True:
            line = f.readline()
            if not line:
                break
            print(line)
except FileNotFoundError:
    print("파일을 찾을 수 없습니다")