# 튜플 만들기 () 사용
t1 = (1,2,3)
print(t1)
print(type(t1))

t2 = 4,5,6 # () 사용하지 않아도 됨
print(t2)

t3 = t1, (7,8,9)
print(t3) # ((1, 2, 3), (7, 8, 9))

t4 = [1,2], [3,4]
print(t4) # ([1, 2], [3, 4])

t5 = tuple([5,6,7,8]) # 리스트를 튜플로 변환
print(t5)

###
li1 = list(t1)
print(li1)

# 튜플을 리스트로 변환
to_list1 = list(t3)
print(to_list1) # [(1, 2, 3), (7, 8, 9)]

to_tuple = tuple([[1,2,3],7,8,9])
print(to_tuple) # ([1, 2, 3], 7, 8, 9)

# 튜플의 변경
t = (1,2,3)
# t[0] = 3 # TypeError: 'tuple' object does not support item assignment
# print(t)

print(to_tuple) # ([1, 2, 3], 7, 8, 9)
# to_tuple[0] = [5,7,9]   # TypeError: 'tuple' object does not support item assignment
to_tuple[0][1] = 3 # 튜플은 변경이 안되지만 튜플 내에 있는 리스트 형태의 값을 변경하는 것은 가능함
print(to_tuple)

####
# 원소 3을 갖는 튜플 t10을 생성하시오
t10 = (3,)
t11 = 3,
# t12 = tuple(3)  # TypeError: 'int' object is not iterable
t12 = tuple([3])
print(t10,t11,t12)


