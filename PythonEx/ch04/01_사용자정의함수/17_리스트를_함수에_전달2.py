# 17_리스트를_함수에_전달2.py

def show_list(my_list) :
    print('함수 내부에서 출력1 : ', my_list)
    my_list[0] = 10 # 리스트 부분변경
    print('함수 내부에서 출력2(리스트 부분변경 후) : ', my_list)
    print("함수 내부 출력, id : ", id(my_list))
    # 함수내에서 매개변수  my_list의 전체요소값을 변경
    my_list=[100,200,300] # 결과는 새로운 지역변수 my_list가 새로 메모리를 받아 생성됨
    print('함수 내부에서 출력3(리스트 전체변경 후) :', my_list)
    # 원본 리스트 전체에 새로운 값 저장 시
    # 원본 리스트(전달된 전역변수)가 전체 요소를 변경하는 게 아니고
    # 새로운 리스트 생성
    print("함수 내부 출력, id : ", id(my_list)) # id가 전역변수와 다르게 나타남-함수 종료되면 메모리 소멸

my_list=[1,2,3,4]
print("함수외부(호출전)에서 출력 1 : ", my_list)
show_list(my_list)
print("함수 외부(호출후)에서 출력 2 : ", my_list)
print("함수 외부 출력, id : ", id(my_list))

# 함수 내/외부에서 동일한 리스트를 사용하고자 하면 global을 사용해 주던가 전체 리스트 대입은 하지 말아야 함