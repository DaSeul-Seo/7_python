s = "I Like Python. I Like Java Also"

# count() : 문자열 내 검색어 개수를 반환
# find() : 문자열 내 첫번째 검색된 위치의 인덱스를 반환
# index() : 문자열 내 검색된 위치의 인덱스를 반환
# rindex() : 문자열 내 오른쪽으로부터 검색된 위치의 인덱스를 반환
# startswicj() : 문자열이 지정된 검색어로 시작하는지 여부 반환
# endswich() : 문자열이 지정된 검색어로 끝나는지 여부 반환

print(s.count('Like')) # 2

print(s.find('Like')) # 2
print(s.find('Like',5)) # 17
print(s.find('JS')) # -1
print(s.rfind('Like')) # 17

# print(s.index('JS'))
print(s.rindex('Like')) # 17

print(s.startswith('I Like')) # True
print(s.startswith('Like', 2)) # True
print(s.endswith('Also')) # True
print(s.endswith('Java',0,26)) # True