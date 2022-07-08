# 스태틱/클래스 메서드 : @staticmathod / @classmethod 키워드 사용
# 클래스명.메서드로 접근

class Math :
    @staticmethod # 객체 변수를 만들지 않고 함수를 사용할 수 있음
    def add(a,b):
        return a+b

    @staticmethod
    def multiply(a, b):
        return a * b

# 클래스 메서드로 사용
print("클래스메서드로 접근 : ", Math.add(10,20))
print("클래스메서드로 접근 : ", Math.multiply(10,20))

# 일반 객체 메서드로 접근
m_o = Math() #객체 인스턴스 생성
print("객체 메서드로 접근 : ", m_o.add(10,20))
print("객체 메서드로 접근 : ", m_o.multiply(10,20))