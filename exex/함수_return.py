# [return]
# 함수를 종료시키고, 해당 함수를 호출한 곳으로 되돌아 가게 한다.
# 파이썬에서는 어떤 종류의 객체도 반환할 수 있다.
# 여러 객체를 return하면 튜플로 반환한다.
# return문을 만나면 함수는 종료
# return문만 사용하면 None을 반환
# 함수가 끝날 때까지 종료할 필요가 없고 반환할 값이 없을 때는 return문이 없어도 된다.

# 인수 없이 반환하기
def do_nothing():
    return # None을 반환

# return 문이 필요없는 경우도 있다
def say_hello():
    print("Life is too short, You need Python")

# 한 개의 값을 반환
def max_value(a, b):
    if a > b:
        return a
    else:
        return b

# 여러 값을 반환할 때
def swap(a, b):
    return b, a

print(swap(10, 20))
# 결과값은 튜플로 반환된다

print(do_nothing()) # None
say_hello()
print(max_value(10,5))

# [인수의 전달 방법]
# 기본적으로 참조에 의한 호출(Call-by-reference)
# 하지만 인수의 타입이 변경가능(mutable), 변경불가(immutable)에 따라 처리 방식이 달라진다.

# 변경 가능 객체를 인수로 전달할 경우
def g(t):
    t[0] = 0
a = [1, 2, 3]
g(a)
print(a) # [0,2,3]

# 변경 불가 객체를 인수로 전달했을 때
def h(t):
    t = (10, 20, 30)
a = (1, 2, 3)
h(a)
print(a) # a 객체는 변경되지 않는다 # (1,2,3)