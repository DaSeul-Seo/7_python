# 문자열의 format메소드를 이용하면 좀 더 편리한 방식으로 문자열 포맷을 지정
# format_map 메소드를 이용하면 이름 기반으로 map의 데이터 형식을 이용 포맷을 지정

a = "I have {} apples, and I ate {} apples.".format(5,3)
b = "I have {total} apples, and I ate {num} apples.".format(total = 5, num = 3)
c = "I have {total} apples, and I ate {num} apples.".format_map({"total": 5, "num": 3})

print(a) # I have 5 apples, and I ate 3 apples.
print(b)
print(c)