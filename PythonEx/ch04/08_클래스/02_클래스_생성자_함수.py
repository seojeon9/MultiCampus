# 생성자 함수
# 클래스라는 개념을 만들어 낼때 반드시 필요하다하고 약속된 특수 함수

# 개발자가 안만들면 번역기가 무조건 정의함

# 파이썬에서 생성자 함수를 만들기 위해서는
# __init__(self)

class Person :
    # 객체 변수를 생성할 때 한번 호출 됨
    def __init__(self): # self 현재 클래스(모듈) 자신을 지칭함
        # print(self, 'is generated')
        # Person의 속성을 생성
        self.name = 'Kata'
        self.age = 10
    def __str__(self):
        return '{},{}'.format(self.name,self.age)

p1 = Person()
print(p1)

class Rectangle :
    # 객체 변수 생성할 때 한번 호출됨
    def __init__(self):
        print(self, 'is generated')
        self.width = 1
        self.height = 1

# # 생성자 함수 호출하는 방법 : 객체변수를 생성
# p1 = Person() # p1 객체변수 생성자 함수 호출
# p2 = Person() # p2 객체변수 생성자 함수 호출
#
# print(p1.name) # p1이 사용할 수 있는 변수 name을 생성했음
# print(p2.name) # p2이 사용할 수 있는 변수 name을 생성했음
#
# p1.name = 'Hong'
# p2.name = 'Lee'
# print(p1.name)
# print(p2.name)
#
# p2.age = 36
# p2.age = 25
#
# r1 = Rectangle()
# r2 = Rectangle()
#
# print(r1.width, r1.height)
# r1.width = 10; r1.height=20
# print(r1.width, r1.height)
#
# print(r2.width, r2.height)
# r2.width = 100; r2.height=30
# print(r2.width, r2.height)
#
# # test
# l1= list((1,2,3))