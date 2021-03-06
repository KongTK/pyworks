# 키보드로 조종하기
import turtle as t

def turn_right():
    t.setheading(0) # 오른쪽 화살표 각도 = 0
    t.forward(10)
def turn_up():
    t.setheading(90) # 위쪽 화살표 각도 = 90
    t.forward(10)
def turn_left():
    t.setheading(180)
    t.forward(10)
def turn_down():
    t.setheading(270)
    t.forward(10)

t.shape("turtle")
t.onkeypress(turn_right, "Right") # 키 조종 함수, turn_right의 ( )생략
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.listen() # 실행 대기

t.mainloop()