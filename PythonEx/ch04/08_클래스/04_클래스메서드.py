class Person :
    # 객체 변수를 생성할 때 한번 호출 됨
    def __init__(self, name='이서정', age=24, sex='F'): # self 현재 클래스(모듈) 자신을 지칭함
        print('self : ', self)
        # Person의 속성을 생성
        self.name = name # 초기값
        self.age = age
        self.sex = sex
    def sleep(self): # 파라미터가 한 개 있는 메서드, 단, 첫번째 파라미터는 클래스의 포인터를 전달받는다.
        print('self : ', self)
        print(self.name,'은 잠을 잡니다.')

class Rectangle :
    # 객체 변수 생성할 때 한번 호출됨
    def __init__(self, width, height):
        print(self, 'is generated')
        self.width = width
        self.height = height
    def calcArea(self): # 파라미터가 한 개 있는 메서드, 단, 첫번째 파라미터는 클래스의 포인터를 전달받는다.
        area = self.width * self.height
        return area

###########################################
# class 객체 생성 및 사용
a = Person('Aaron',20,'M')
b = Person('Bob',30)

print(a)
print(b)

a.sleep()
b.sleep()

# Rectangle 클래스 사용
r_a = Rectangle(10,30)
r_b = Rectangle(3.5,2.2)

print("면적 r_a : ", r_a.calcArea())
print("면적 r_b : ", r_b.calcArea())