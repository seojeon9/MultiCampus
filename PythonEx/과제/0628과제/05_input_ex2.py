#  다음과 같이 무게와 키 값을 입력 받아서 BMI 지수를 계
# 산하는 프로그램 작성
#  BMI = 몸무게 / 키의 제곱

weight = float(input("몸무게(킬로그램): "))
height = float(input("키(미터): "))

BMI = weight / height**2

print("당신의 BMI : %0.2f" % BMI)