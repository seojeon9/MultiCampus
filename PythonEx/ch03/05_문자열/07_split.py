# split()
# 구분자를 기준으로 문자열을 나눔
# 리스트로 반환
# 구분자 : 기본은 공백
# 구분자 지정 : “-”, “:”, “,”, …

string = "Python Programming"
str_split = string.split() # 기본 사용 : 공백 기분 분리
print(str_split) # ['Python', 'Programming'] list로 반환

names = '홍길동,이몽룡,성춘향,변학도'
name_split = names.split(",")   # 구분자로 , 사용
print(name_split)    # ['홍길동', '이몽룡', '성춘향', '변학도']

colors = "red:blue:yellow:green"
color_split = colors.split(":")
print(color_split)  # ['red', 'blue', 'yellow', 'green']