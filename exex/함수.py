# [함수]
# 입력값을 가지고 어떤 일을 수행한 다음 그 결과물을 내 놓는 것
# <함수를 사용하는 이유>
# 반복되는 부분이 있을 경우 재활용
# 프로그램 흐름을 일목요연하게 볼 수 있다.

# [함수 정의하기]
# Def키워드 이용해 정의
# 함수 이름과 인수들이 기술
# 함수 선언부는 :로 끝난다.
# 들여쓰기 규칙이 적용
# 함수의 끝은 들여쓰기가 적용 안되는 라인에서 끝난다.

def dummy():
    pass # 실행할 내용이 없을때는 pass
def my_function():
    print("Hello World")
def times(a, b):
    return a * b # 결과값을 돌려줘야 할 때는 return 문으로 반환
def do_nothing():
    return # return 문만 썼을 경우, None이 반환
dummy()
my_function()
print(times(10, 10))
print(do_nothing())

# [함수도 객체다]

t = times
print(t(100, 100)) #10000
print(t, times, sep = ",")
#<function times at 0x102fe14d0>,<function times at 0x102fe14d0