# 속성
# 사전 구성을 위한 딕셔너리 ek_dic
# 사전을 저장하기 위한 파일명 file_name

# 메서드
# 검색을 위한 메서드 : search(self), dict_search(self,eng)
# 구성을 위한 메서드 : const_dict(self), input_dict(self,eng)
# 저장 및 로딩을 위한 메서드 : save_dict(self), load_dict(self)

class Dict_Const :
    # 생성자 함수 - 객체 인스턴스 생성시 사전을 저장하거나 불러올 파일명을 인수로 받는다
    def __init__(self, file_name):
        self.file_name = file_name # 사전을 저장하기 위한 파일명
        self.ek_dic = {} # 사전 구성 dict


    def const_dict(self):
        while True:  # 단 사전등록은 사용자가 원하는 만큼 등록이 간으하게 할 것이므로 무한루프 사용
            # 영어단어 입력 받기
            eng = input("\n영어 단어 입력 : (종료는 'q') : ")

            # 종료검사
            if eng == 'q':
                print('단어 등록을 종료합니다. ')
                break  # 반복 종료 (반복문 외에 함수에 다른 문장 없으므로 함수 종료)
            elif eng not in self.ek_dic:  # 등록되지 않은 단어
                # 단어 등록 처리 함수 호출
                self.input_dict(eng)
            else:
                print("%s는 이미 등록된 단어입니다. " % eng)

    def input_dict(self,eng):
        # 단어에 해당하는 뜻 입력 받기
        kor = input(eng + " 뜻 입력 : ")
        # 사전에 등록
        self.ek_dic[eng] = kor
        # 반환값이 필요 없고 출력 값도 필요없음

    def dict_search(self,eng):  # 단어가 사전에 있는 경우 호출
        print("%s의 뜻은 %s입니다. " % (eng, self.ek_dic[eng]))

    def search(self):
        # 검색 단어 입력 받기
        eng = input("\n검색할 단어 입력 : ")

        if eng in self.ek_dic:  # 사전에 있는 단어면
            self.dict_search(eng)
        else:
            print("%s는 사전에 없는 단어입니다. " % eng)
            # 사전 등록 여부
            answer = input('사전에 등록 하시겠습니까?(y/n)')
            if answer == 'y':
                self.input_dict(eng)
                print("사전 등록 완료! 감사합니다!")
            print("\n 검색 종료 합니다.")

    def load_dict(self):
        # 사전파일은 초기에 빈파일을 하나 생성해 놓고 시작함
        # 사전 읽어오는 함수
        # 사전파일 읽어오기
        f = open("./res/"+self.file_name+".txt", "r", encoding='utf-8')
        results = f.readlines()
        # print(results)
        f.close()
        if results == []:
            return 0
        # 저장을 한행에 한문장으로 저장하기 때문에 리스트는 비어있거나 요소가 1개가 있음
        res = results[0].split("-")  # 키와 value 나누기

        # 키 분할
        d_key = res[0].split(',')[:-1]  # 키 분할시 나타나는 무의미한 빈문자열 제거 후 저장
        # 값 분할
        d_value = res[1].split(',')[:-1]

        # 분할된 키와 값을 딕셔너리로 구성
        dict_temp = dict(zip(d_key, d_value))
        # print(dict_temp)
        # ek_dic = dict_temp # 공용변수에 저장하려 했으나 지역변수 ek_dic 가 새로 생성되버림
        # ek_dic가 딕셔너리이므로 아이템을 추가하는 방식으로 부분변경
        for item in list(dict_temp.items()):
            k, v = item
            self.ek_dic[k] = v  # 공용변수 ek_dic 를 부분 변경
        # 공용변수에 dict_temp의 item들을 저장
        print('사전 준비 완료!!!!')

    def save_dict(self):
        # 사전을 파일로 저장(쓰기)하는 함수
        # dog,cat,-강아지,고양이,
        result = ''
        f = open('./res/'+self.file_name+'.txt', 'w', encoding='utf-8')
        # ek_dict의 키 - value 형태로 구성
        d_key = self.ek_dic.keys()  # key만 추출
        d_value = self.ek_dic.values()  # value만 추출

        # key를 문자열로 저장
        for k in d_key:
            result += k + ','
        # value와 구분자 추가
        result += '-'
        for v in d_value:
            result += v + ','
        # 파일에 쓰기
        f.write(result)
        f.close()
        print('사전 저장 완료!!!')