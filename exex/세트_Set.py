# 순서가 없고 중복이 없는 객체들의 집합(non sequence). {} 기호로 정의
    # len(), in, not in 정도만 활용
# 수정이 가능한(mutable) 자료형
# 수학의 집합을 표현할 때 사용

a = {1,2,3}
print(a, type(a))

print(len(a))
print(2 in a)
print(2 not in a)

# add(x) : 세트에 x를 수가
# remove(x) : 세트에서 x를 제거. x가 세트에 없으면 오류 발생
# discard(x) : 세트에서 x를 제거. x가 세트에 없으면 무시
# update({set}) : 세트에 여러 개의 값을 추가
# clear() : 세트를 비움

s = {1, 2, 3}
s.add(4)
print(s) # {1, 2, 3, 4}
s.add(1)
print(s) # {1, 2, 3, 4}
s.discard(2)
print(s) # {1, 3, 4}
s.remove(3)
print(s) # {1, 4}
s.update({2, 3})
print(s) # {1, 2, 3, 4}
s.clear()
print(s) # set()