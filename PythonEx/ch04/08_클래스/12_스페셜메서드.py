# Point 클래스 :
# 2차원 좌표평면 각 점(x,y) 표현하는 속성 x,y
# 기능(연산)
# 두 점의 덧셈과 뺄셈

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 두점의 덧셈 : (1,2) + (3,4) = (4,6)
    def __add__(self, pt):
        new_x = self.x + pt.x
        new_y = self.y + pt.y
        return Point(new_x, new_y)

    # 두점의 뺄셈 : (1,2) + (3,4) = (-2,-2)
    def __sub__(self, pt):
        new_x = self.x - pt.x
        new_y = self.y - pt.y
        return Point(new_x, new_y)

    # 한 점과 숫자의 곱셈
    def __mul__(self, factor):
        return Point(self.x * factor, self.y * factor)

    # x,y 값 가져오기[]인덱스 사용가능하게 해줌
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            return -1

    def __setitem__(self, index, data):
        if index == 0:
            self.x = data
        elif index == 1:
            self.y = data
        else:
            print("out of range")

    # 좌표 0,0으로 부터의 거리
    def __len__(self):
        import math
        res = int(math.sqrt(self.x ** 2 + self.y ** 2))
        return res

# x,y 값 출력
    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

####################################
# Point 객체 인스턴스 생성 후 특별 메서드를 이용한 연산

p1 = Point(3,4)
p2 = Point(2,7)

# __add__
print(p1.__add__(p2))
p3 = p1 + p2 # p1과 p2가 포인트 클래스 이므로 포인트 클래스에서 재정의 해 놓은 __add__ 규칙이 적용됨
print(p3)

print(3+5) # int 클래스에서 재정의해 놓은 __add__의 규칙이 적용됨

print(p1.__sub__(p2))
p4 = p1 - p2# p1과 p2가 포인트 클래스 이므로 포인트 클래스에서 재정의 해 놓은 __sub__ 규칙이 적용됨
print(p4)

# p1 -=> (3,4)
print(p1.__mul__(p2))
p5 = p1 * p2# p1과 p2가 포인트 클래스 이므로 포인트 클래스에서 재정의 해 놓은 __mul__ 규칙이 적용됨
print(p5)

print(p1)
print(p1.__getitem__(0))
print(p1[0])
print(p1.__getitem__(1))
print(p1[1])
print(p1[2]) # 값이 없어서 -1

# (3,4)
p1.__setitem__(0,5)
print(p1[0])
print(p1)


