# AirPlane 클래스
class AirPlane:
    # 기본 생성자는 생략가능
    def takeoff(self):
        print("비행기가 이륙합니다")
    def fly(self):
        print("비행기가 일반 비행합니다")
    def land(self):
        print("비행기가 착륙합니다")

class SuperSonicPlane(AirPlane):
    NORMAL = 1
    SUPERSONIC = 2

    def __init__(self):
        self.flymode = SuperSonicPlane.NORMAL # 상수도 클래스 이름으로 접근

    def fly(self):
        if self.flymode == SuperSonicPlane.SUPERSONIC:
            print("비행기가 초음속 비행을 합니다")
        else:
            super().fly() # 부보 매서드 상속 시에 super로 받음

sa = SuperSonicPlane()
sa.takeoff()
sa.fly()
sa.flymode = SuperSonicPlane.SUPERSONIC
sa.fly()
sa.land()
