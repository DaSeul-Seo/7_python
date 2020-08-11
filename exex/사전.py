# 순서를 가지지 않는 객체의 집합
# Key 기반으로 값을 저장하고 참조하는 매핑형 자료형
# 시퀀스 자료형이 아니므로 len(), in, not in정도만 가능

d = {'basketball': 5, 'soccer': 11, 'baseball': 9}
print(d, type(d)) # {'basketball': 5, 'soccer': 11, 'baseball': 9} <class 'dict'>
print(d['basketball']) # 5
d['volleyball'] = 6
print(d) # {'basketball': 5, 'soccer': 11, 'baseball': 9, 'volleyball': 6}
print(len(d)) # 4
print('soccer' in d) # True
print('volleyball' not in d) # False

# 다양한 사전 생성 방법
d = dict() # empty dict
print(d) # {}
d = dict(one=1, two=2) # keyword arguments
print(d) # {'one': 1, 'two': 2}
d = dict([('one', 1), ('two', 2)]) # tuple list
print(d) # {'one': 1, 'two': 2}
keys = ('one', 'two', 'three')
values = (1, 2, 3)
d = dict(zip(keys, values)) # 키와 값을 별도로 선언 후 합침
print(d) # {'one': 1, 'two': 2, 'three': 3}