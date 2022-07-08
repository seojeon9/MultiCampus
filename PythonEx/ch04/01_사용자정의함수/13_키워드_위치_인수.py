# 13_키워드 위치_인수

# 학생의 이름 나이 성별자료를 입력받아 딕셔너리로 구성 후 반환하는 함수
def student_info(name, age, gender) :
    student = {
        'name' : name,
        'age' : age,
        'gender' : gender
    }
    return student

# 호출 테스트(위치인수, 키워드 인수 연습)
print(student_info(name='kim', age=24, gender='여')) # 키워드 인수
print(student_info('lee', 25,'남')) # 위치 인수
print(student_info('hong', gender='여', age=22))
print(name) # 함수 안에서 사용된 변수를 밖에서 사용할 수 없음

# 위치인수 지정 후 키워드 인수  # SyntaxError: positional argument follows keyword argument
# print(student_info(gender='남', 'park', 28)) # 키워드 인수 뒤에 위치인수가 오면 에러발생
# print(student_info('lee',age=25,'남')) # 매개변수와 순서가 동일해도 키워드인수가 위치인수보다 앞에 나오면 에러
# print(student_info('lee', '남',age=25)) # TypeError: student_info() got multiple values for argument 'age'
# '남' 두번째 인수기 때문에 매개변수 age에 대입되고 age=25 인수에 의해 age에 또 대입

