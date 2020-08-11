# packing과 unpacking
# Packing : 나열된 객체를 Tuple로 저장하는 것
# Unpacking : 튜플, 리스트 안의 객체를 변수로 할당하는 것

t = 10, 20, 30, 'python'
print(t) # (10, 20, 30, 'python')
print(type(t)) # <class 'tuple'>
# unpacking tuple
a, b, c, d = t
print(a, b, c, d) # 10 20 30 python
# unpacking list
a, b, c, d = [10, 20, 30, 'python']
print(a, b, c, d) # 10 20 30 python

# 확장 unpacking
# Unpacking 시 왼쪽 변수가 부족한 경우, 에러가 발생한다(ValueError)
# 확장 Unpacking에서는 왼쪽 변수가 적은 경우에도 적용할 수 있다 (*)

# a, b = (10, 20, 30, 40, 50) # ValueError 발생
t = (1, 2, 3, 4, 5, 6)
a, *b = t
print(a, b) # 1 [2, 3, 4, 5, 6]
*a, b = t
print(a, b) # [1, 2, 3, 4, 5] 6
a, b, *c = t
print(a, b, c) # 1 2 [3, 4, 5, 6]
a, *b, c = t
print(a, b, c) # 1 [2, 3, 4, 5] 6