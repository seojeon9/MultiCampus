# 2개의 숫자를 전달 받아서 연산 결과를 반환하는 함수를 생성하시오
# add()/sub()/mul()/div()

def add(num1,num2) :
    return num1 + num2

def sub(num1,num2) :
    return num1 - num2

def mul(num1,num2) :
    return num1 * num2

def div(num1,num2) :
    return num1 / num2

# 함수 호출 테스트
num1 = int(input('숫자1을 입력하세요 : '))
num2 = int(input('숫자2을 입력하세요 : '))

print("더한 결과 ",add(num1,num2))
print("뺀 결과 ",sub(num1,num2))
print("곱한 결과 ",mul(num1,num2))
print("나눈 결과 ",div(num1,num2))