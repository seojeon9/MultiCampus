# 집합은 중복된 요소가 있을 수 없고 순서가 없기때문에 인덱스를 사용할 수 없다
# 집합 만들기
s1 = {1,2,3,4,5}
print(s1)
print(type(s1)) # <class 'set'>

# set() 함수로 집합만들기
s2 = set([10,20,30])
print(s2)
print(type(s2))

s3 = set((100,200,300))
print(s3)
print(type(s3)) # <class 'set'>

# 집합은 동일한 요소(값)이 중복 될 수 없다
s4 = {1,2,3,3,4}    # 에러 발생하지 않는다.
print(s4) # {1, 2, 3, 4} # 중복된 값 제거하고 집합 생성

# 수집한 데이터들의 중복갑 빼고 사용하고 싶을 때 set 함수 이용하면 간편

#
# s5 = {1,2,[3,4]}    # TypeError: unhashable type: 'list'
s6 = {1,2,(3,4)}
print(s6)

#
# print(s3[0])    # TypeError: 'set' object is not subscriptable : 부분접근 불가능하다
s = {1,2,3}
# 집합의 요소 추가 : add() 1개 추가시
s.add(4)
print(s)
# 여러 요소 추가 : update([])
s.update([5,6])
print((s))

# 요소 삭제 : remove/descard
s.remove(3)
print(s)

s.discard(5)
print(s)    # {1, 2, 4, 6}

# 없는 요소 삭제시
# s.remove(10) # KeyError: 10
s.discard(10) # 에러 없음, 작업을 하지 않는다.

# 전체 요소 삭제
s.clear()
print(s)    # set() 빈집합

# 집합 완전 삭제
del s #삭제됨
# print(s)    # NameError: name 's' is not defined. Did you mean: 's1'?

# 집합 연산 정리
A= {1,2,3}
B= {3,4,5}

# 합집합
C = A|B
print(C)

C= A.union(B)
print(C)

#교집합
C = A&B
print(C)

C= A.intersection(B)
print(C)

#차집합
C = A-B
print(C)

C= A.difference(B)
print(C)

C = B-A
print(C)

C= B.difference(A)
print(C)
