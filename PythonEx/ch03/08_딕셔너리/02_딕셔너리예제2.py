# 딕셔너리 선언
dict_cook = {
    "name" : "버섯 불고기 덮밥",
    "type" : "덮밥",
    "ingredient" : ["소고기","버섯","양파","간장","설탕"],
    "origin" : "한국"
}

# 딕셔너리 내용 출력
print("요리명 : ", dict_cook["name"])
print("종류 : ", dict_cook["type"])
print("재료 : ", dict_cook["ingredient"])

# 딕셔너리 값 변경
dict_cook["name"] = '한우 버섯 불고기 덮밥'
print("요리명 : ", dict_cook["name"])

# 새 아이템 추가
dict_cook["amount"] = 50000
