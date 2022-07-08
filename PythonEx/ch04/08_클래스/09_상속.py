
# 부모 클래스
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self, food):
        print('{}은 {}를 먹습니다.'.format(self.name, food))

    def sleep(self, minute):
        print('{}은 {}분동안 잡니다.'.format(self.name, minute))

    def work(self, minute):
        print('{}은 {}분동안 일합니다.'.format(self.name, minute))

# 자식 클래스인 Student와 Employee를 생성(Person클래스 상속)
# 생성자 함수는 다시 선언해서 각 클래스의 속성을 재구성

# Person클래스 상속받아 Student 클래스 생성
# 상속 형식
# class 자식클래스명(부모클래스명) :

class Student(Person) :
    # Student속성 name과 age는 재구성
    # 생성자함수 이용
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person) :
    # Employee속성성 name과 age는 재구성
    # 생성자함수 이용
    def __init__(self, name, age):
        self.name = name
        self.age = age

bob = Employee('Bob', 25)
lee = Student('Lee', 19)

bob.sleep(30) # Person 부모클래스의 sleep()메서드를 사용할 수 있다
lee.work(30) # Person 부모클래스의 work()메서드를 사용할 수 있다