# 회원 정보를 입력받아 딕셔너리 생성 후 반환해주는 함수

def get_info() :
    name = input("이름 입력 : ")
    age = input("나이 입력 : ")

    student = {'name' : name, 'age':age}

    return student

# 호출 테스트
student_info = get_info()
print(student_info)