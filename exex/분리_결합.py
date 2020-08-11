# split() : 문자열을 공백문자(혹은 지정된 문자)를 기준으로 분리
# rsplit() : 문자열을 공백문자(혹은 지정된 문자)를 기준으로 오른쪽부터 분리
# join() : 문자열을 지정된 기호로 합침
# splitlines() : 문자열을 개행문자를 기준으로 분리

s = 'spam and ham'
t = s.split()
print(t) # ['spam', 'and', 'ham']
t = s.split(' and ')
print(t) # ['spam', 'ham']

s2 = ":".join(t)
print(s2) # spam:ham

s3 = "one:two:three:four:five"
print(s3.split(':', 2)) # ['one', 'two', 'three:four:five']
print(s3.rsplit(':', 2)) # ['one:two:three', 'four', 'five']

lines = '''1st line
2nd line
3rd line
4th line
'''
print(lines.splitlines()) # ['1st line', '2nd line', '3rd line', '4th line']