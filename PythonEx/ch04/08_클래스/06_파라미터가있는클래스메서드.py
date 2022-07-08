class Rectangle :
    # 객체 변수 생성할 때 한번 호출됨
    def __init__(self, width, height):
        print(self, 'is generated')
        self.width = width
        self.height = height
    # instance 메서드 - 객체(인스턴스)를 이용해서 호출
    def calcArea(self,width,height): # 파라미터가 한 개 있는 메서드, 단, 첫번째 파라미터는 클래스의 포인터를 전달받는다.
        if width > 0 and height > 0 :
            area = width * height
        else :
            area= self.width * self.height
        return area

r_1 = Rectangle()

print('r_1의 면적 : ', r_1.calcArea(5,3))