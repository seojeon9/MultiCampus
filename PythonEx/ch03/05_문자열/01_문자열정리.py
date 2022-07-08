# 문자열(String) : 문자의 나열
# 작은따옴표, 큰따옴표, 삼따옴표 사용해서 문자열 생성
# 한문자가 한개의 메모리 칸에 저장되고 저장된 문자들을 연결해서 관리를 한다.

crawling = 'Data crawling is fun'
parsing = "Data parsing is also fun"

print(crawling) ; print(parsing)
print(type(crawling)) ; print(type(parsing))    # <class 'str'>

# 연산자 사용 : (+, *)

# + 연산자 : 문자열과 문자열 연결(결합)
"홍길동" + "서울" # 2개의 문자열을 결합해서 1개의 문자열 "홍길동서울"로 변환
print("홍길동" + "서울")

name = "홍길동"
address = "서울"

cont = name + address # cont에는 두 문자열이 결합된 1개의 문자열이 저장

# * 연산자 : 곱하는 수 만큼 문자열을 반복해서 하나의 문자열로 생성
string = "파이썬"
result = string * 3
print(result)

# 문자열 인덱싱(indexing)
# 인덱스로 문자의 위치를 나타내는 것
# 인덱스(첨자) : 문자의 위치, 0부터 시작
# string[0] : 0번 위치 (첫번째 문자)
# string[-1] : 마지막 문자

# crawling = 'Data crawling is fun'
# parsing = "Data parsing is also fun"

print(crawling[5])
print(crawling[-1])

# 슬라이싱(slicing)
# 문자열 중에서 일부분을 복사해서 참조하는 것
# 원본 문자열 중 일부를 복사해서 반환
# 문자열 원본 변수는 변경할 수 없다.
# : 기호를 이용해서 사용
# string[start index : stop index + 1]
print(parsing[3:6])


