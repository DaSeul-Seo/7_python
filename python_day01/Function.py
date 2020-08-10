def f(x): # 함수선언
    return x+10

var=f(10) #함수 호출
print(var) # 20출력

def division(x):
    if x%2: # 나머지가 존재할 경우
        return True
    else: # 나머지가 0일 경우
        return False

    print('running') # 절대 실행되지 않음

var1 = division(10)
var2 = division(11)

print(var1)
print(var2)
