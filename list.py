# 리스트는 list([])의 형태로 생성하거나 []를 이용해 만들 수 있음
# 시스트는 연속된 데이터를 표현하는 방법

# 리스트 생성
var = list([1,2,3,4,5])
print(var)
var1=[1,2,3,4,5]
print(var1)
print()

# 인덱싱, 슬라이싱
var2=[1,2,"3",4,5,6]
print(var2[0])
print(var2[2])
print(var2[0:4])
print()

# split()은 문자열을 리스트로 바꿔주는 함수
var3 = "hello world"
print(var3.split())
print()

# 리스트를 문자열로 변환
a=["1","2","3","4","5"]
b=".".join(a)
print(b) # 1.2.3.4.5
print()

# 리스트 연산 덧셈과 곱셈 연산만 가능
var4 = [1,2,3,4,5]
var5 = [6,7,8,9,10]
num=3
print(var4 * 3) # 계산을 해주는 것이 아니라 1,2,3,4,5를 3번 반복
print(var4 + var5)

