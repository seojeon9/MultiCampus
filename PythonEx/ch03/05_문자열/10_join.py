# join()
# 각 문자 사이에 특정 문자(열) 삽입

a = "aa"
print(a.join("bbb"))    # baabaab
print(a)

a = "-"
print(a.join("abcd"))   # a-b-c-d : 구분자를 삽입할 수 있는 함수

# join의 대상이 list 일 수 있다
sep = "-"
names = ["홍길동", "이몽룡", "성춘향"]
print(sep.join(names))  # 홍길동-이몽룡-성춘향
print(type(sep.join(names)))    # <class 'str'>

# join은 문자열 함수이다.
sep = "-"
numbers = [10,20,30,40,50]
# print(sep.join(numbers))    # 숫자는 에러
# TypeError: sequence item 0: expected str instance, int found