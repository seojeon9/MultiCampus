# 모든 프로그램 언어는 문자가 나열되어 있으면 식별자로 인식함
# abc NameError: name 'abc' is not defined. Did you mean: 'abs'?

abc = 0
abc

# 변수에 저장 할 값이 문자인 경우 따옴표를 사용해서 문자데이터라는 것을 명시해야 함
"d@@@eh"
str_1 = 'deh'
print(str_1)

name = "홍길동"
age = 23
print(name, age)
address = '서울시 강남구'
print(name + '은 ' + address + "에 삽니다")  # 문자열 결합연산 후 출력  #연산기호에 의해 문자열들이 더해진 후 출력이 일어남
print(name , '은 ' , address , "에 삽니다")  # 각 변수와 문자열 리터럴들을 각각 출력 #출력을 하나씩 출력을 함 (,에 따라 4번 출력)

# print(name + "은" + age + "살 입니다")
# TypeError: can only concatenate str (not "int") to str
# 문자열과 숫자는 결합(+) 할 수 없다

# 문자열과 숫자의 결합(연결) : 숫자를 형변환시켜 사용 가능
# 23 => "23" : 숫자를 문자열으로 형변환
# str(변수명/숫자) -> 문자열로 변환된 결과를 돌려 줌
print(name + "은 " + str(age) + "살 입니다.")
print(type(age))