# 조건분기는 조건에 따라 코드의 실행 유무를 결정지어줌
# if키워드 사용
# 파이썬은 끝나는 것이 없어서 들여쓰기로 블럭 구분 ==> 들여쓰기 중요!

# if문 기본구조
condition_t = True
condition_f = False

if condition_t: #True이기 때문에 아래 2개 print 실행
    print('hello')
    print('world')
if condition_f: #False이기 때문에 아래 2개 print 실행 안함
    print('HELLO')
    print('WORLD')

print('last')
print()

# if-else활용
condition1 = True
condition3 = True
condition2 = True

if condition1:
    print('첫번째 조건')
elif condition2:
    print('두번째 조건')
elif condition3:
    print('세번째 조건')
else:
    print('네번째 조건')

# in을 활용해 포함유무 검사
if 'h' in 'hello world': #True
    print('hello world에 h가 포함되어 있습니다.')
if 1 in [11,22,33,44,55,66]: #False
    print([11,22,33,44,55,66], '에 1이 포함됩니다.')
