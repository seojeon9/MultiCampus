# 문자열의 접근 방법 : 인덱싱과 슬라이싱을 이용해서 접근
crawling = 'Data crawling is fun'
parsing = "Data parsing is also fun"

print(crawling) # 문자열 전체
print(crawling[:]) # 문자열 전체

print(crawling[0:4]) # 0 ~ 3
print(crawling[5:16]) # 5 ~ 15
print(crawling[17:]) # 17인덱스 글자부터 마지막 글자까지

print(crawling[-1:]) # 마지막 글자
print(crawling[:-1]) # 0번 인덱스 글자(첫글자)부터 마지막 문자, 전문자(끝에서 두번째 문자)

# parsing[3:6] = "abc"
# TypeError: 'str' object does not support item assignment
# 문자열 부분 변경은 불가능 하다