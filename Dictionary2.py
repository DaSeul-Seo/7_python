# Key: value 추가
var={}
print(var) #{}
var["key1"] = 10
print(var) #{'key1':10}
var["key1"] = 20
var["key2"] = 30
print(var) #{'key1':20, 'key2':30}
print()

# setdefault()를 활용해 키가 존재하지 않을 때만 추가
var1={}
print(var1)
var1.setdefault('key1', 10)
print(var1)
var1.setdefault('key1', 20)
var1.setdefault('key2', 30)
print(var1)
print()

# key 리스트 라져오기
var2={'key1': 'value1', 'ket3':'value3'}
print(var.keys()) # dict_keys(['key1','key2;])
print()

# value 리스트 가져오기
var3 = {'key1':'value1', 'key2':'value2'}
print(var.values()) # dict_values(['value1','value2'])
print()

# key-value한쌍으로 리스트 가져오기
var4 = {'key1':'value1', 'key2':'value2'}
print(var.items()) # dict_itmes([('key1','value1), ('key2','value2')])

# key존재유무 검사
var5={'key1' : 'value1', 'key2':'value2'}
print('key1' in var5) # Ture
print('hello' in var5) # False
