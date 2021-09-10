# Person 클래스

class Person:
    # 매개 변수가 있는 생성자
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "이름 : {0}, 나이 : {1}".format(self.name, self.age)

class Employee(Person): # person을 상속받음
    pass

# main()
p1 = Person("손흥민", 30) # p1 : 인스턴스(=객체)
print(p1.name, p1.age)
p2 = Person("김연아", 31)
print(p2)

emp1 = Employee("흥부", 30)
print(emp1.name) # employee는 따로 정의하지 않았지만 person을 상속받아 person의 소속을 employee 객체가 사용 가능
print(emp1.age)
print(emp1)

emp2 = Employee("놀부", 35)
print(emp2)