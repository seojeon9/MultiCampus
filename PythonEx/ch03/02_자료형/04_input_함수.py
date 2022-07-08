# 사용자로부터 사각형의 높이와 길이를 입력받아서 사각형 면적을 출력하는 프로그램을 작성하시오.

# 키보드를 통한 data의 입력에 사용하는 기능(함수) : input()
# 형식 : input("입력 가이드 문자열")
# 주의 : 키보드를 통한 입력은 문자열로 입력이 됨 - 입력된 데이터로 연산하려면 형변한이 필요하게 됨
# width = input("사각형의 가로 길이는? ")
# heigh = input("사각형의 세로 길이는? ")
#
# # print(type(width), type(heigh))
#
# print("사각형의 면적은", int(width)*int(heigh), "입니다.") # 계산 당시에만 형변환

# Q. width, heigh 변수의 data type은? str 형태
# print(type(width), type(heigh))

# width = int(input("사각형의 가로 길이는? "))
# heigh = int(input("사각형의 세로 길이는? "))
#
# print(type(width), type(heigh))
#
# print("사각형의 면적은", width * heigh, "입니다.")

##################
# x = float(input("실수 입력 : "))
# y = x * 3
# print(y)

##### 입력되는 숫자 모양 그대로 사용하려면 : eval() 함수

# width = eval(input("사각형의 가로 길이는? "))
# heigh = eval(input("사각형의 세로 길이는? "))
#
# print(type(width), type(heigh))
#
# print("사각형의 면적은", width * heigh, "입니다.")

# eval() 함수는 수식 입력해도 됨
a = eval(input("수식 입력 : "))
print(a)
print(type(a))