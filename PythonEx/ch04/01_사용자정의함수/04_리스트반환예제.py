# 반환 값으로 리스트 사용 예제
# 사용자로부터 3명의 회원명을 리스트에 입력받아 리스트를 반환하는 예제

def get_names() :
    names = [] # 회원명 입력할 빈 리스트

    for i in range(3) :
        name = input("이름 입력 : ")
        names.append(name)

    return names # 리스트 반환

# 함수 호출 테스트
# name_list = get_names()
# print(name_list)

# 함수 호출 테스트
# for name in range(len(get_names())) :
#     print(name)

# 함수 호출 테스트
for name in get_names() :
    print(name)

# 더미 멀티 리턴 함수
def multi_return_t() :
    return [1,2,3] # 리스트 리터럴 반환

# print(multi_return_t())
