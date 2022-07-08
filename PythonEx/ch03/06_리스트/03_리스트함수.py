# len/count 함수
a = [1,2,3,3,5]
print("원소의 개수 : ", len(a)) # 5
print("원소 3의 개수 : ", a.count(3)) # 2

# append() / insert() => 새로운 요소 추가
# append() : 리스트의 끝에 새로운 요소 추가
# 리스트.append('추가할값') : 마지막 원소로 추가
a = [1,2,3,4]
a.append(5)
print(a)

a.append([6,7]) # 마지막에 하위 리스트 추가
print(a)

# 마지막에 2개의 원소 추가
# a.append(8,9)
# TypeError: list.append() takes exactly one argument (2 given)

# 빈 리스트 생성하고 요소 나중에 추가
values = []
values.append(10)
values.append(20)
values.append(30)
print(values)

# for문 사용하여 요소 추가
scores = []
for i in range(5) :
    scores.append(i)
# 리스트 출력
print(scores)

# insert() : 리스트의 특정 위치에 요소 삽입
# 리스트.insert(위치, 값)
# a.insert(1,5)   # 새로운 값이 정해진 위치에 들어가고 기존 값들의 위치는 한칸씩 뒤로 밀림
# print(a)

nums = [1,2,3,4,5]
nums.insert(1,200) # 두번째에 삽입
print(nums) # [1, 200, 2, 3, 4, 5]

# 마지막이었던 자리에 원소 삽입
nums.insert(-1,"홍길동")
print(nums) # [1, 200, 2, 3, 4, '홍길동', 5]

# 찐 마지막에 원소 삽입
nums.insert(len(nums), 12.3) # len(nums) -> 7 [0~6,7]
print(nums) # [1, 200, 2, 3, 4, '홍길동', 5, 12.3]

nums.insert(len(nums)-1, [10,20]) # 마지막 원소 앞에 하위 리스트 삽입
print(nums)

# removw() / pop() : 리스트 요소 제거
# 리스트.remove(값) : 값이 리스트에 있으면 리스트에서 제거함
# 단, 동일한 값이 여러개 있는 경우 첫 번째 값만 제거
# 다 제거하려면 반복문 사용
n = [1,2,3,3,4,5,4,3]
n.remove(4) # 첫번째 찾아지는 4를 제거
print(n)    # [1, 2, 3, 3, 5, 4, 3]

# 동일한 원소를 한꺼번에 제거
n = [1,2,3,3,4,5,4,3]
# for i in range(len(n)) :
#     n.remove(4) # ValueError: list.remove(x): x not in list
#     # 반복 횟수를 리스트 원소수만큼 설정했고 삭제 할 값이 더이사 없으면 에러가 발생
# print(n)

# 삭제하려고 하는 값의 개수를 count 함수를 이용해 확인
count = n.count(3)
for i in range(count) :
    n.remove(3)
    print(i+1, "번째 3 삭제 : ", n)
print(n)    # [1, 2, 4, 5, 4]

# pop() : 리스트의 마지막 요소 반환하고 삭제
x = ['a', 'b', 'c', 'd']
y = x.pop() # 리스트의 마지막 요소 반환하고 그 요소를 리스트에서 삭제
print(y) # d
print(x)    # ['a', 'b', 'c']
x.pop()
x.pop()
x.pop()
print(x) # [] : pop 계속해서 더아상 요소가 없으면 빈 리스트가 남는다
# x.pop() # IndexError: pop from empty list
# print(x)

# pop(인덱스) : 인덱스 위치에 있는 요소 반환하고 해당 요소 삭제
heroes = ['슈퍼맨', '스파이더맨', '헐크', '아이언맨']
print(heroes.pop(2)) # 세번째 헐크가 삭제
print(heroes)

# extend() : 리스트 확장
# 이전리스트에 원소를 추가해서 확장된 리스트로 변경시킴

a = [1,2,3]
# a.append((4,5)) #[1,2,3,[4,5]) 새로 추가한 리스트가 하위 리스트로 추가
a.extend([4,5]) # [1, 2, 3, 4, 5]
print(a)

# sort()/reverse()/sorted() : 정렬 함수

# sort() : 리스트 정렬(기본 오름차순 정렬), 원본 반영
# sort(reverse=True) : 리스트 정렬(내림차순 정렬)
scores = [90,78,81,64,89]
scores.sort()
print(scores)   # [64, 78, 81, 89, 90]

# reverse()
# 원소의 위치를 역순으로 변경(정렬은 하지 않고 원소들의 순서만 바꾼다)
scores = [90,78,81,64,89]
scores.reverse()
print(scores)   # [89, 64, 81, 78, 90]

# sorted() : 원본 유지하면서 정렬된 새로운 리스트를 반환(파이썬 내장함수)
scores = [90,78,81,64,89]
print(sorted(scores))   # [64, 78, 81, 89, 90]
print(scores)   # [90, 78, 81, 64, 89]

# 문자의 정렬
# 영문자의 정렬
char = ['b', 'A', 'd', 'C']
char.sort() # ['A', 'C', 'b', 'd']
print(char)

# 대소문자 구별 없이 정렬
char = ['b', 'A', 'd', 'C']
char.sort(key=str.lower)  # ['A', 'C', 'b', 'd']
print(char)

# 대소문자 구별없이 내림차순 정렬
char = ['b', 'A', 'd', 'C']
char.sort(key=str.lower,reverse=True)
print(char)

# 문자열의 정렬
ids = ['SKY', 'Blue', 'red', 'eBook', 'GREEN']
ids.sort()
print(ids)  # ['Blue', 'GREEN', 'SKY', 'eBook', 'red']

ids = ['SKY', 'Blue', 'red', 'eBook', 'GREEN']
ids.sort(key=str.lower)
print(ids)  # ['Blue', 'eBook', 'GREEN', 'red', 'SKY']

test = ['black', 'brown', 'blue']
test.sort()
print(test) # ['black', 'blue', 'brown']

# max() 최대값/ min() 최소값 함수
n = [100, 7, -2, 99, 30]
print("최대 : ", max(n))
print("최소: ", min(n))

# 문자는
c = ['c', 'a', 'D', 'A', 'b']
print("최대 : ", max(c))
print("최소: ", min(c))

# 문자열
s = ['hello', 'Apple', 'zea']
print("최대 : ", max(s))
print("최소: ", min(s))

# index(찾을 값) : 리스트 안에서 특정 원소를 찾아 원소의 위치값(인덱스) 반환
# 원소가 존재하지 않으면 에러

names = ['홍길동', '이몽룡']
print(names.index('이몽룡'))
# print(names.index('박지성'))   # ValueError: '박지성' is not in list

# in / not in : 포함 여부를 판단
# True / False 반환
print('홍길동' in names) # True
print('박지성' in names) # False

# 리스트 일치 검사
list1 = [1,3,5]
list2 = [1,3,5]
list3 = [1,4,5]
print(list1 == list2)
print(list1 == list3)