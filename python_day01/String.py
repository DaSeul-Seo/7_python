var1 = "파이썬"
print(var1) # 파이썬
print()

var2="hello"
var3 ="world"
var4=var2+ "" + var3 #var2과 var3 합함
print(var2)
print(var3)
print(var4) # var3과 var4를 합한 var4출력
print()

var = "hello world!"
print(var)
var=var.replace('!','?') # !를 ?로 바꿈
print(var)
print()

var5='hello world'
finded1 = var5.find('a')
finded2 = var5.find('world')
print(finded1) # -1출력. 찾지목하면 -1을 출력
print(finded2) # 6출력. 몇번째 있는지 알려줌
print()

var6 = "hello world"
print(var6[0]) # h출력. 인덱싱하기
print(var6[1]) # e출력. 인덱싱하기
print(var6[0:4]) #hell 출력. 슬라이싱하기
print(var6[-6:]) # world!
print()

var7="hello world"
print(var7[:]) # hello world 출력
print(var7[:2]) # he 출력
print(var7[2:]) #llo world
