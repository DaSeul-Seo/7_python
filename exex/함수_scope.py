# [스코핑 룰(Scope)]
# 이름공간(Namespace)
#   - 프로그램에서 사용되는 이름들이 저장되는 공간
# 이름은 값을 치환할 때 해당 값의 객체와 함께 생겨나고 이름공간에 저장
# 이름공간에 저장된 이름을 통해 객체를 참조
# 이름공간의 종류
#   - Local Scope: 함수내부
#   - Enclosed: function in finction
#   - Global: 모듈내부
#   - Built-in: 내장 영역
# 동일한 이름이 여러 영역에 있다면 LEGB순으로 찾는다.

x = 1
def func(a):
    return a + x # Local 스코프에 x 가 없으므로 Global x를 사용한다
def func2(a):
    x = 2
    return a + x # Local 스코프에 x가 있으므로 Local x를 사용한다

print(func(10)) # 11
print(func2(10)) # 12
print(x) # 1
# ----------------------------------------------------------------------

# 함수내부에서 전역 객체를 사용해야 하는 경우 global 선언문을 이용
# 가능하면 함수 내부에서 글로벌 객체를 직접 사용하는 것은 피한다.

g = 1
def func3(a):
    global g
    g = 3 # 본 객체는 글로벌 객체이다
    return a + g
print(func3(10)) # 13
print(g) # 3