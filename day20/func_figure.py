# 도형의 면적을 계산하는 함수

# 사각형의 면적을 계산하는 함수
def square(w, h):
    area = w * h
    return area
# 삼각형의 면적을 계산하는 함수
def triangle(w, h):
    area = w * h / 2 # 10.0으로 나오기때문에 10(정수)으로 표현하고 싶으면 int()사용
    return area

# 너비가 5cm, 높이가 4cm인 사각형의 넓이 계산
area_rec = square(5,4) # area라고 선언하여도 return area와 다른 area 변수
print("사각형의 면적 : ", area_rec)
area_tri = triangle(5,4)
print("삼각형의 면적 : ", area_tri)
