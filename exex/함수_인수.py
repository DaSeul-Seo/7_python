# 인수는 필요한 개수만큼 선언할 수 있다.
# 기본값이 필요하면 함수 선언시 지정할 수 있다.

def sum(a, b):
    return a + b

def incr(a, step = 1): # 두 번째 인자의 기본값은 1
    return a + step

print(sum(2, 3)) # 5
print(incr(10)) # 두 번째 인자의 기본값을 사용한다 # 11
print(incr(10, 2)) # 두 번째 인자를 직접 지정한다 # 12

# ----------------------------------------------------------------
# [키워드 인수]
# 인수값을 인수 이름으로 전달할 수 있다.(함수의 정의에 따른다)
def area(width, height):
    return width * height

print(area(10, 12)) # 120
print(area(height = 4, width = 3)) # == area(3, 4) # 12

# ----------------------------------------------------------------
# [가변인수]
# 정해지지 않은 개수의 인수값을 받을 때 사용
# 선언 시 인수명 앞에 *를 붙여 선언
def get_total(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(get_total(1, 3, 5, 7, 9)) # 25

# ----------------------------------------------------------------
#[사전 키워드 전달]
# 정해지지 않은 키워드 인수는 모두 dict로 받을 수 있다.
# 선언 시 인수명 앞에 **를 붙인다.
# 사전 키워드 인수는 선언의 맨 마지막에 있어야 한다.
def f(a, b, *args, **kwd):
    print(a, b) # 10, 20
    print(args) # (30, 40)
    print(kwd) # {'depth': 10, 'dimension': 3}
f(10, 20, 30, 40, depth = 10, dimension = 3)

# ----------------------------------------------------------------
# 함수객체를 인수로 전달
# 파이썬에서는 함수도 객체이다.
# 따라서 인수로 함수를 전달하는 것도 가능
states = ['Alabama', ' Georgia', 'Georgia ', 'georgia', 'FlOrIda',
'south carolina ', 'West virginia']
def clean_strings(strings, *funcs): # 함수 목록을 가변인수로 전달
    results = []
    for string in strings:
        for func in funcs: # 전달된 함수들을 순차적으로 적용
            string = func(string)
        results.append(string)
    return results

states = clean_strings(states, str.strip, str.title)
print(states) # ['Alabama', 'Georgia', 'Georgia', 'Georgia', 'Florida', 'South Carolina', 'West Virginia']
