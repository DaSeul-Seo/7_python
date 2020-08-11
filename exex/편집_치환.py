s = '  apam and ham  '

# center() : 문자열을 가운데로 정렬
# ljust() : 문자열 왼쪽으로 정렬
# rjust() : 문자열 오른쪽으로 정렬
# zfill() : 자리수를 지정하고 빈 공간을 0을 채움

print(s.center(60))
print(s.center(60, '-'))
print(s.ljust(60,'-'))
print(s.rjust(60,'-'))

print('20'.zfill(5)) # 00020
print('1234'.zfill(5)) # 01234