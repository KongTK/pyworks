# Person2 클래스 정의

class Person:
    # 매개 변수가 있는 생성자
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "이름 : {0}, 나이 : {1}".format(self.name, self.age)

class Employee(Person):
    def __init__(self, name, age, empid):
        super().__init__(name, age) # 부모 멤버는 super()로 받음
        self.empid = empid

    def __str__(self):
        return "이름 : {0}, 나이 : {1}, 사번 : {2}".format(self.name, self.age, self.empid)

emp1 = Employee("콩쥐", 25, 1001)
print(emp1)