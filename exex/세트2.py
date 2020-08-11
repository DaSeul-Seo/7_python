# 교집합, 합집합, 차집합

# 교집합(set) | a&b | a.intersection(b)
# 합집합(set) | a|b | a.union(b)
# 차집합(set) | a-b | a.difference(b)
# 모집합(bool) |  | a.issuperset(b)
# 부분집합(bool) |  | a.issubset(b)

s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {10, 20, 30}
s3 = s1.union(s2) # 합집합
print(s3) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30}
s4 = s1.intersection(s2) # 교집합
print(s4) # {10}
s4 = s1.difference(s2) # 차집합
print(s4) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
s5 = s1.symmetric_difference(s2)
print(s5) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 30}
print(s1.issuperset(s4)) # True
print(s5.issuperset(s1)) # False
print(s2.issubset(s3)) # True