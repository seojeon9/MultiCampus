# 리스트 복사
# 얕은 복사 : 실제 리스트는 복사되지 않고 참조값(주소)만 복사
# 복사본 리스트 요소의 값을 변경하면 원본 리스트 요소의 값도 변경

scores = [10,20,30,40]
values = scores
values[0] = 100 # 복사본 리스트의 요소 값 변경

print("scores : ", scores)  # 원본 리스트의 요소값도 변경됨
print("values : ", values)

# 깊은 복사(원본 보관)
# - 연산자는 깊은 복사가 진행이 안됨
# list() 함수 또는 deepcopy()함수를 사용해서 리스트 값의 복사본을 새로 생성해야함 (참조에서 벗어나 공간이 하나가 더 생기는 것임)
scores = [1,2,3,4,5]
values = list(scores)
values[0] = 100 # 복사본 리스트의 요소 값 변경

print("scores : ", scores)  # 원본 리스트의 요소값도 변경 없음
print("values : ", values)

# deepcopy() : 깊은 복사 - copy 라이브러리에 포함되어 있음
import copy
a = ['a', 'b', 'c']
b = copy.deepcopy(a)

b[0] = 1
print(a)
print(b)