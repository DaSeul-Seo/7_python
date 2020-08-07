# for문을 이용한 반복문은 while문과 다르게 조건을 넣지 않음

# for 구조
# for 변수 in range(0,10):
#     실행코드1
# for 변수 in(리스트 or 문자열 or 딕셔너리 or 튜플):
#     실행코드1

# range()를 이용한 반복문
for i in range(0,5):
    print('%d 번째'%(i))

print()

# 문자열을 이용한 반복문
for i in 'hello world':
    print(i)

print()

# 리스트를 이용한 반복문
for i in [11,22,33,44,55]:
    print(i)

print()

# 딕셔너리를 이용한 반복문
var={'key1':'value1','key2':'value2'}
for key in var:
    print(key)
    print(var[key])
    