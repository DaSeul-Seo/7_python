# 사전 메소드
# keys() : 사전내 키 목록을 dict_keys 객체로 반환
# values() : 사전내 값 목록을 dict_values 객체로 반환
# items() : 사전내 키-값 쌍을 튜플로 묶은 dict_items 객체로 반환
# get(key {,default}) : 사전내 key에 대응하는 값을 반환
#                         default를 지정하면 key에 대응하는 값이 없을 때 default를 반환
# del dic[key] : dic 사전 내 key에 대응하는 객체를 삭제
# clear() : 사전을 비움
## dict_keys, dict_values, dict_items 를 리스트로 사용하려면 list() 함수를 활용

d = {'basketball': 5, 'soccer': 11, 'baseball': 9}
d['volleyball'] = 6 # 새로운 값 할당
print(d.keys()) # key 목록 가져오기
# dict_keys(['volleyball', 'baseball', 'soccer', 'basketball'])

print(d.values()) # Value 목록 가져오기
# dict_values([6, 9, 11, 5])

print(d.items()) # (key, value) 튜플 목록 가져오기
# dict_items([('volleyball', 6), ('baseball', 9), ('soccer', 11), ('basketball', 5)])

# ---------------------------------------------------------------------------------
di = {'basketball': 5, 'soccer': 11, 'baseball': 9}
di['volleyball'] = 6
print(di.keys()) # dict_keys(['basketball', 'soccer', 'baseball', 'volleyball'])
print(di.values()) # dict_values([5, 11, 9, 6])
print(di.items()) # dict_items([('basketball', 5), ('soccer', 11), ('baseball', 9), ('volleyball', 6)])
# x = di['handball'] # KeyError
x = di.get('handball') # None 반환
print(x) # None
del di['soccer']
print(di) # {'basketball': 5, 'baseball': 9, 'volleyball': 6}
di.clear()
print(di) # {}

# 사전 순회 ----------------------------------------------------------------------
dict = {'basketball': 5, 'soccer': 11, 'baseball': 9}
for key in dict:
    print(str(key) + ":" + str(dict[key]), end = ' ') # basketball:5 soccer:11 baseball:9
else:
    print()

for key in dict.keys():
    print("{0}:{1}".format(key, dict[key]), end = ' ') # basketball:5 soccer:11 baseball:9
else:
    print()

for key, value in dict.items():
    print("{0}:{1}".format(key, value), end = ' ') # basketball:5 soccer:11 baseball:9
else:
    print()