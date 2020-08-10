# 튜플은 리스트와 매우 흡사하지만 데이터의 변경 및 삭제가 불가능
# tuple(())또는 ()을 이용해 튜플 생성 가능
# 변경 및 삭제를 제외하고 리스트와 동일하게 작동함

# 튜플 생성
var1=tuple((1,))
var2=tuple((1,2,3))
var3=(1,)
var4=(1,2,3)
print(var1)
print(var2)
print(var3)
print(var4)
print()

# 튜플에서 데이터 수정을 시도한다면?
# var5=(1,2,3)
# print(var5)
# var5[0]=10
# # TypeError
# print()

# 인덱싱 및 슬라이싱
var6 = (1,2,3,4,5)
print(var6[3]) # 4
print(var6[2:]) #(3,4,5)
print()

# 리스트처럼 덧셈 및 곱셈 연산 가능
var7=(1,2,3,4,5)
var8=(11,22,33,44,55)
print(var7)
print(var8)
print(var7+var8)
print(var7*3)
print(var8*3)
