# 클래스 정의하기
# 인스턴스(클래스객체변수)를 생성하기 위해서는 모체가 되는 클래스 정의
# class 클래스명 :
#   클래스 생성자
#   클래스 속성(변수, 특성)
#   클래스 메서드(기능, 함수)

# person 클래스 정의
# 빈 클래스로 정의
class person :
    pass

class Rectangle :
    count = 0 # 클래스 속성

    def __init__(self): # 클레스 생성자
        Rectangle.count += 1

    def print_count(self):  # self 외부에서 오는 매개변수가 아니라 자체적으로 만든 매개변수 -> 매개변수가 없는거임
        self.count

# print_count 클래스 내부에 있는 함수기 때문에 객체 인스턴스 생성 후 사용해야 함

# 클래스 객체 인스턴스(객체변수) 생성
# 변수명 = 클래스명([생성자매개변수])
rect1 = Rectangle()

# 객체변수 rect1을 이용해 메서드 print_count()
rect1.print_count()
rect1.count

rect2 = Rectangle()
rect3 = Rectangle()

######### 파이썬 내부 클레스 사용 예제
### 형변환 함수
a = '123'
# int는 클래스 이름 아래코드는 int 클래스 생성자 함수를 호충
int_a = int(a) # int_a는 int클래스의 인스턴스(객체 변수)

b = 123
str_b = str(b)

str_b.replace('1','a')
