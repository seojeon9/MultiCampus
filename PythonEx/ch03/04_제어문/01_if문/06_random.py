# 랜덤 숫자 생성(난수)
# 난수는 파이썬 기본 기능은 아니고 기본 제공되는 모듈로 사용해야 함
# 해당 모듈(랜덤)은 import 해서 사용해야 함
from random import randint

# randint(최소, 최대) : 최소부터 최대 사이의 임의의 정수 반환
n1 = randint(1,5)
print(n1)