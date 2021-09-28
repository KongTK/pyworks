# raise 구문 - 예외 처리 미루기
# 사용하는 쪽에서 예외 처리를 해야 함

class Animal:
    def cry(self):
        raise NotImplementedError # 상속받는 클래스가 받드시 구현해야 함
    def breath(self):
        print("숨을 쉽니다")
    
class Dog(Animal):
    # pass
    def cry(self):
        print("왈왈")

class Cat(Animal):
    # pass
    def cry(self):
        print("야옹")

dog = Dog() # 상속
dog.cry()   # 부모 매서드 사용
dog.breath()

cat = Cat()
cat.cry()
cat.breath()