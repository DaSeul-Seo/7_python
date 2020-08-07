# 딕셔너리는 리스트와 다르게 순서가 존재하지 않음
# 딕셔너리는 key:value쌍으로 이루어진 데이터 타임
# 딕셔너리는 key를 이용해 데이터 접근
# dict({})또는 {}을 사용해 만들 수 있음

# 딕셔너리 생성 및 키로 데이터 접근
var1 = dict({"key1" : "value1", "key2" : "value2"})
var2 = {"key1" : "value1", "key2" : "value2"}
print(var1)
print(var2)
print(var1["key1"])
print(var2["key2"])
print()

# 만약 존재하지 않는 키를 접근한다면?
var = {'key' : 'value1'}
print(var['key2']) # KeyError: 'key2'

# get()을 활용해 키가 존재하지 않을 때 기본 값 출력
var3 = {'key1' : 'value1'}
print(var3.get('key1'))
print(var3.get('key1', 'default value'))
print(var3.get('key2'))
print(var3.get('key2','default value'))
