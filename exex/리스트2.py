# append(x) : 리스트의 마지막에 x를 추가
# insert(i,x) : 리스트의 인덱스 i위치에 x를 추가
# reverse() : 리스트를 역순으로 뒤집음
# sort() : 리스트 요소를 순서대로 정렬
# remove(i) : 리스트 인덱스 i에 있는 요소 제거
# extend(l) : 리스트 마지막에 리스트 l를 추가
# index(x) : 인덱스 내에 x가 있으면 인덱스 값을 반환. 없으면 -1
# count(x) : 리스트 내에 x가 몇 개 있는지 그 개수를 반환

a = [1, 2, 3]
print(a) # [1, 2, 3]
a.append(5)
print(a) # [1, 2, 3, 5]
a.insert(3, 4) # 인덱스 3에 요소 4를 추가
print(a) # [1, 2, 3, 4, 5]
print(a.count(2)) # 리스트 내 요소 2의 개수를 반환 # 1
a.reverse()
print(a) # [5, 4, 3, 2, 1]
a.sort()
print(a) # [1, 2, 3, 4, 5]
a.remove(3) # 내부에 있는 요소 3을 제거
print(a) # [1, 2, 4, 5]
a.extend([6, 7, 8])
print(a) # [1, 2, 4, 5, 6, 7, 8]

b = [1,5,3,9,8,4,2]
b.sort()
print(b) # [1, 2, 3, 4, 5, 8, 9]

b.sort(reverse=True)
print(b) # [9, 8, 5, 4, 3, 2, 1]

# 키값 기반의 사용자 정의 정렬
c = [10,2,22,9,8,33,4,11]
c.sort(key = str)
print(c) # [10, 11, 2, 22, 33, 4, 8, 9]

c.sort(key = int)
print(c) # [2, 4, 8, 9, 10, 11, 22, 33]