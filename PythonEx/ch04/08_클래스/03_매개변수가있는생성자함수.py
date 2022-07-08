# __init__(self,초기값파라미터1, 초기값파라미터2,....)
# 기본값을 줄 수 있음
class Person :
    # 객체 변수를 생성할 때 한번 호출 됨
    def __init__(self, name='이서정', age=24, sex='F'): # self 현재 클래스(모듈) 자신을 지칭함
        print(self, 'is generated')
        # Person의 속성을 생성
        self.name = name # 초기값
        self.age = age
        self.sex = sex

class Rectangle :
    # 객체 변수 생성할 때 한번 호출됨
    def __init__(self, width, height):
        print(self, 'is generated')
        self.width = width
        self.height = height
    def calc(self):
        print('계산합니다')

############## Person 인스턴스 생성
p1 = Person('김철수', 25, 'M')
p2 = Person('홍길동', 30)
p3 = Person()

print(p1.name, p1.age, p1.sex)
print(p2.name, p2.age, p2.sex)
print(p3.name, p3.age, p3.sex)

############## Rectangle 인스턴스 생성
r1 = Rectangle(3,4)
r2 = Rectangle(10,2)

print(r1.width,r1.height)
print(r2.width,r2.height)
# r1.calc(123) # TypeError: Rectangle.calc() takes 1 positional argument but 2 were given