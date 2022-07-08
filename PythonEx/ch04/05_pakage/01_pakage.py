# import mypack.pack1.module11
# mypack.pack1.module11.function11()

# 패키지 모듈명이 너무 길면 별칭 사용
# import mypack.pack1.module11 as mm1
# mm1.fuction11()

from mypack.pack2.module21 import function21 # 함수명
function21()

from mypack.pack3.module31 import * # 모든 함수를 import
function31()