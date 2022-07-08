# 함수 인수로 리스트 사용
def show_names(names) :
    for name in names :
        print(name, end=' ')
# 함수 인수를 딕셔너리 사용
def show_info(info) :
    print(info)
    print("이름 : " + info['name'])

### 함수 호출 테스트
info_list={'name':'kim','age':23}
name_list=['둘리','길동','철수']

show_info(info_list)
show_names(name_list)