# 인자
# 함수 호출 시 값을 함수에게 전달할 수 있음

# 함수 호출 시 값 전달
def f(x,y):
    print('running ' + str(x)+ ' ' + str(y))
    return True

var1 = f(10,11)
print(var1)

#  함수 호출시 인자가 맞지 않는다면? TypeError

# 함수 기본 값 설정
def f(x,y=20):
    print('running ' + str(x) + ' ' + str(y))
    return x+y

var1 = f(10)
var2 = f(10,40)

print(var1) # 30
print(var2) # 50
