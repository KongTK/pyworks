# 접근 제한 - 멤버(private), 함수(public)
# 접근 방법 - get + 멤버이름(), set + 멤버이름()
class Student:
    def __init__(self, name):
        self._name = name # _붙이면 은닉 가능
        self._grade = 0

    def learn(self):
        print("학생이 배웁니다")

    def getname(self):
        return self._name

    def setgrade(self, grade):
        self._grade = grade

    def getgrade(self):
        return self._grade

s1 = Student("흥부")
s1.setgrade(2)
# s1.name = "놀부"  클래스 정보가 이렇게 쉽게 변경되면 안되기 때문에 접근 제한(_)을 추가
print("이름 :", s1.getname())
print("학년 :", s1.getgrade())