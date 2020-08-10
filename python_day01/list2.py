# 리스트 마지막에 요소 추가
var6 = [1,2,3,4,5]
var6.append(10)
print(var6) # [1,2,3,4,5,10]
var6.append(20)
print(var6) # [1,2,3,4,5,10,20]
print()

# 리스트 마지막 요소 제거
var7 = [1,2,3,4,5]
print(var7.pop()) # 5
print(var7) # [1,2,3,4]
print()

# sort()를 이용해 정렬가능 문자는 아스키코드로 매핑되어 정렬됨
var8=['a','b','c','d']
var8.sort()
print(var8)
var8.sort(reverse=True)
print(var8)
print()

# 정렬 시, 문자와 숫자가 섞여 있다면 에서 발생
# a=[75,"a","A", 98, 100]
# print(a.sort())
# print()

# 리스트 길이
var9=[1,2,3,4,5,6,7]
print(len(var7)) #7
