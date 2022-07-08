# dict_inout.py
# 사전 읽어오기, 사전 저장하기 기능
from .dict_var import ek_dic # 프로그램 실행중 사전 데이터를 갖고있는 변수
def load_dict() :
    # 사전파일은 초기에 빈파일을 하나 생성해 놓고 시작함
    # 사전 읽어오는 함수
    # 사전파일 읽어오기
    f = open("./res/eng_dict.txt","r",encoding='utf-8')
    results = f.readlines()
    # print(results)
    f.close()
    if results == [] :
        return 0
    # 저장을 한행에 한문장으로 저장하기 때문에 리스트는 비어있거나 요소가 1개가 있음
    res = results[0].split("-") # 키와 value 나누기

    # 키 분할
    d_key = res[0].split(',')[:-1] #키 분할시 나타나는 무의미한 빈문자열 제거 후 저장
    # 값 분할
    d_value = res[1].split(',')[:-1]

    # 분할된 키와 값을 딕셔너리로 구성
    dict_temp = dict(zip(d_key,d_value))
    # print(dict_temp)
    # ek_dic = dict_temp # 공용변수에 저장하려 했으나 지역변수 ek_dic 가 새로 생성되버림
    # ek_dic가 딕셔너리이므로 아이템을 추가하는 방식으로 부분변경
    for item in list(dict_temp.items()) :
        k,v = item
        ek_dic[k] = v # 공용변수 ek_dic 를 부분 변경
    # 공용변수에 dict_temp의 item들을 저장
    print('사전 준비 완료!!!!')

def save_dict() :
    # 사전을 파일로 저장(쓰기)하는 함수
    # dog,cat,-강아지,고양이,
    result = ''
    f=open('./res/eng_dict.txt','w',encoding='utf-8')
    # ek_dict의 키 - value 형태로 구성
    d_key =ek_dic.keys() # key만 추출
    d_value = ek_dic.values() # value만 추출

    # key를 문자열로 저장
    for k in d_key :
        result += k+','
    # value와 구분자 추가
    result += '-'
    for v in d_value :
        result += v+','
    # 파일에 쓰기
    f.write(result)
    f.close()
    print('사전 저장 완료!!!')