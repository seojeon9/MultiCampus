# 딕셔너리 만들기
# key : value로 이루어짐
d = {1:'a'}
print(d);print(type(d)) #<class 'dict'>

# 딕셔너리 요소(아이템) 추가
# 딕셔너리[새로 추가될 아이템의 키] = 저장할 값
d[2] = 'b'
print(d)    # {1: 'a', 2: 'b'}

# key는 문자도 가능
# 연락처 구성위해 딕셔너리 생성(이름, 전화버호 저장)
member = {'name':'홍길동', 'phone':'01012345678'}
print(member)   # {'name': '홍길동', 'phone': '01012345678'}

# 주소 아이템 추가
member['address'] = '서울'
print(member)   # {'name': '홍길동', 'phone': '01012345678', 'address': '서울'}

print("--------------------------")

naver = {
    "name" : "naver",
    "url" : "www.naver.com",
    "userid" : "nv",
    "password" : "1234"
}

google = {
    "name" : "google",
    "url" : "www.google.com",
    "userid" : "gg",
    "password" : "1234"
}

print(naver)
print(google)

print("--------------------------")
# keys()/values()/items()
print(naver.keys())
print(naver.values())
print(naver.items())
# dict_keys(['name', 'url', 'userid', 'password'])  # 리스트가 dict_keys로 감싸져 있다
# dict_values(['naver', 'www.naver.com', 'nv', '1234'])
# dict_items([('name', 'naver'), ('url', 'www.naver.com'), ('userid', 'nv'), ('password', '1234')]) # items는 리스트안에 튜플이 들어있고 dict_items로 감싸져 있다

print(type(naver.keys()))   # <class 'dict_keys'>
print(type(naver.values())) # <class 'dict_values'>
print(type(naver.items()))  # <class 'dict_items'>

print("----------------------------")

# 리스트로 변환 : list()함수
to_list = list(naver.keys())
print(to_list) # ['name', 'url', 'userid', 'password']
print(type(to_list)) # <class 'list'>

to_tuple = tuple(naver.keys())
print(to_tuple) # ('name', 'url', 'userid', 'password')
print(type(to_tuple)) # <class 'tuple'>

print()

# 각 요소 출력
# dict_keys/dict_values/dict_items 타입은 반복 요소로 사용가능
for key in naver.keys() :
    print(key)

for value in naver.values() :
    print(value)

for item in naver.items() :
    print(item)

print("-------------------------------")
# key로 value 찾기
print(naver["userid"])
print(naver.get("password"))

# 찾고자하는 key가 딕셔너리에 없으면
# print(naver['link'])    # KeyError: 'link'
print(naver.get("link"))    # None
# link키를 찾아서 있으면 값을 반환 없으면 없음을 반환
print(naver.get("link","없음")) # 없음

# 존재 여부만 확인 : in / not in
print('link' in google)
print('link' not in google)

# 딕셔너리 함수 확인
my_dict = {}
print(dir(my_dict))
# ['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__',
# '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__',
# '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',
# 'setdefault', 'update', 'values']