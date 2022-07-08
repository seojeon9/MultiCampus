#  다음과 같은 함수를 포함하는 프로그램 작성
#  함수명 : show_info()
#  이름, 학년, 나이, 연락처를 전달 받아서 딕셔너리로 만들어 출력

def show_info(name, year, age, phone) :
    dict = {'name':name,'year':year,'age':age,'phone':phone}
    return dict

print(show_info('홍길동',4,23,'010-1234-5678'))