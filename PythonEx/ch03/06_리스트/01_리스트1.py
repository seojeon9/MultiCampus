# 문자열은 부분 원소를 변경할 수 없는데 리스트는 가능
# 배열 -> 똑같은 형태의 데이터가 들어감, 파이썬 기본 자료형에 배열 없음 (numpy라는 패키지에 따로 구성되어 있음)
# 리스트 -> 다른 형태의 데이터 저장 가능

# 리스트 만들기 : [] 이용해서 생성
ints = [1,2,3,4,5]
floats = [1.1,2.2,3.3,4.4,5.5]
names = ["홍길동", "이몽룡", "성춘향", "변학도"]

# 리스트 안에 리스트 포함 가능
numbers = [100,200,300,[10,20,30]]

# 리스트명을 이용해 출력하면 전체 list가 출력 : []포함
print(ints)
print(floats)
print(names)
print(numbers)

# 리스트의 각 원소 출력
for name in names :
    print(name)

# 리스트자체를 반복요소로 사용하지 않고 list 각 원소를 출력해라
for i in range(0,len(ints)) :
    print(ints[i])

for n in range(0,len(numbers)) :
    print(numbers[n])   # 리스트 안에 리스트가 있는 경우 안에 있는 리스트는 1개의 원소임

# 리스트 각각의 값을 변수에 저장
nums = [1,2,3]
a = nums[0]
b = nums[1]
c = nums[2]
print(a,b,c)

a, b, c = nums  # 여러개의 변수에 여러개의 값을 한 번에 넣을 수 있음
print(a,b,c)

# 특정 원소에 접근 : 인덱싱
# 인덱스를 통해 리스트 요소를 참조

a = [1,2,3,4,5]
print(a[0]) # 1 : 첫번째 요소
print(a[-1]) # -1 : 뒤에서 첫번째 요소
print(a[-2]) # -2 : 뒤에서 두번째 요소

b = [1,2,3,[10,20]]
print(b[3])
print(b[3][1])
print(b[-1][0])

c = [1,2,3,[10,20],4,5]
print(c[3][1])  # 20 : 4번째 요소의 두번째 요소

# a,b,c 3개의 리스트를 하나로 합치기
all_list = [a,b,c]
print(all_list)
print(all_list[0][2]) # 3 : 첫번째 리스트의 2번째 요소
print(all_list[-1][3][0])

print(names)
print(names[1])
print(names[1][2])

print(names[0:2])   # 리스트의 부분원소 참조(리스트로 반환)
print(names[-1:])   # 마지막 원소를 리스트로 반환 - ['변학도']
print(names[-1])    # 마지막 원소를 문자열로 반환 - 변학도
print(names[-1:][0])    # 0번 인덱스 요소 반환(문자열 변학도)
print(names[-1][0]) # 부분문자열인 '변'이 반환

# 리스트 연산자 ( + / * )
# 리스트 결합 : + 연산자
# 리스트 반복 : * 연산자
# 리스트 내용 변경 : 특정 위치의 요소에 값 저장

a = [1,2,3]
b = [4,5,6]

c = a + b
print(c)    # [1, 2, 3, 4, 5, 6]

d = a*3
print(d)    # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 리스트 내용 변경
a[2] = 30
print(a)

# 리스트내에서 근접한 요소를 한번에 변경하려면 슬라이싱 사용
a[0:2] = [10,20]
print(a)

# 현재 요소에 위치에 리스트를 대입하면 하위 리스트로 생성
b[0] = [1,2,3,4]
print(b)    # [[1, 2, 3, 4], 5, 6]

# 리스트 내용 변경 : 반값(빈리스트) 저장하면 내용 삭제
print(c)
c[1:3] = []
print(c)