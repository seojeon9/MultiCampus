# find 와 index의 차이점 : 찾는 문자열이 없을경우find는 -1을 반환하고 index는 에러가 발생
# 두 메서드 모두 특정 문자열이 있는지 확인하고 있으면(찾아지면) 문자열의 시작위치를 반환

crawling = "Data crawling is fun"

# find()
print(crawling.find("fun")) # 시작위치 17번 인덱스
print(crawling.find("f")) # 시작위치 17번 인덱스
print(crawling.find("parsing")) # 없음 (-1)

cities = "인천 대전 광주 울산 대구 부산"
city = input("우리 나라 광역시 중 하나를 입력해 보세요 : ")

if cities.find(city) != -1 : #존재한다면
    print("정답입니다.")
else :
    print("틀렸습니다.")

# 위 코드와 동일한 표현
if city in cities : #존재한다면
    print("정답입니다.")
else :
    print("틀렸습니다.")

# index() : 위치 반환
# 못찾으면 에러
print(crawling.index("fun")) # 시작위치 17번 인덱스
print(crawling.index("f")) # 시작위치 17번 인덱스
print(crawling.index("parsing")) # ValueError: substring not found 못찾으면 에러