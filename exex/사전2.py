# 사전의 키(key)
# 사전의 키는 해싱해야 하기 때문에 수정 불가능한 객체여야 한다.
# ex) bool, 수치형(int, float, complex), str, tuple

d = {}
print(d) # {}
d[True] = 'true'
d[10] = '10'
d["twenty"] = '20'
d[(1, 2, 3)] = '6'
print(d) # {True: 'true', 10: '10', 'twenty': '20', (1, 2, 3): '6'}
# d[[1, 2, 3]] = '6’ # TypeError 발생