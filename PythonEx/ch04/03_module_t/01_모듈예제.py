# 생성해 놓은 모듈 new_calculator import
import new_calculator # 현재 파일과 동일한 디렉터리내에 존재하므로 바로 찾아짐
# 모듈내 특정 함수 import
# from 모듈명 import 함수명
from new_calculator import sub
from new_calculator import * # 해당 모듈에 있는 모든 함수를 전부 접근할 수 있음
a = new_calculator.add(7,4) # 모듈명으로 import 했으므로 함수 접근은 모듈명.함수명(인수..)
print(a)

s = sub(7,4) #sum 함수를 import 했으므로 앞에 모듈명은 적지 않고 함수명만 적음
print(s)

m = mul(7,4)
m1 = new_calculator.mul(5,6)
d = div(6,3) # 모듈안에 있는 모든 함수를 import 했으므로 함수명만 적어도 인식