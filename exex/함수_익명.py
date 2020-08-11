# 익명함수(Lambda)
# 이름이 정의되지 않은 '익명함수'를 선언
# 데이터 분석/변형 함수에서 파라미터로 처리함수를 인자로 받는 경우가 많다.

def square(x):
    return x * 2
for i in range(10):
    print("{0}:{1}".format(i, square(i)), end = " ") # 0:0 1:2 2:4 3:6 4:8 5:10 6:12 7:14 8:16 9:18
else:
    print()
# Same as above with Lambda
for i in range(10):
    print("{0}:{1}".format(i, (lambda x: x * 2)(i)), end = " ") # 0:0 1:2 2:4 3:6 4:8 5:10 6:12 7:14 8:16 9:18
else:
    print()

# ---------------------------------------------------------------------
# Lambda를 이용한 정렬
# 정렬할 때, key함수로 정의하기에도 편리한 경우가 많다.
strings = ['foo', 'card', 'bar', 'abab', 'aaaa', 'abab', 'foo']
strings.sort(key=lambda x: len(x))
print(strings) # ['foo', 'bar', 'foo', 'card', 'abab', 'aaaa', 'abab']
strings.sort(key=lambda x: strings.count(x))
print(strings) # ['foo', 'bar', 'foo', 'card', 'abab', 'aaaa', 'abab']