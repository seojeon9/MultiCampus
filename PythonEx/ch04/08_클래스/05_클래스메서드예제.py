# 클래스명 : Counter
# 메서드
# 1. 숫자를 하나 증가시키는 기능 : increment()
# 2. 숫자를 0으로 초기화 하는 기능 : reset()
# 3. 현재 count된 숫자를 출력하는 기능 : print_current_value()

# 특성(속성,변수)
# 카운팅 결과를 저장하는 변수 : cnt

class Counter :
    # 생성자 함수 : 카운팅 결과를 저장하는 변수 : cnt 정의
    def __init__(self):
        self.cnt = 0

    # 클래스 메서드 1
    def increment(self):
        self.cnt += 1

    # 클래스 메서드 2
    def reset(self):
        self.cnt = 0

    def print_current_value(self):
        print('현재 카운트된 값은 : ', self.cnt)

#############
# Counter 클래스 생성

c1 = Counter()
c2 = Counter()

c1.increment()
c1.increment()

c2.increment()
c2.increment()

c1.increment()

c1.print_current_value()
c2.print_current_value()
c2.increment()
c2.reset()
c2.increment()

c1.print_current_value()
c2.print_current_value()