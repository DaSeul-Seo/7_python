import re

# 전화번호 추출
test_num = "저의 전화번호는 010-2038-9914입니다"

pattern = re.compile('[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]')
pattern1 = re.compile('\d\d\d-\d\d\d\d-\d\d\d\d')
pattern2 = re.compile('\d{3}-\d{4}=\d{4}')
c = pattern.findall(test_num)
d = pattern1.findall(test_num)
e = pattern2.findall(test_num)
print(c)
print(d)
print(e)

test_str="""I am Park Jeong-tae. I live in Paju.
I lived in Paju for 25 years.
Sample text for testing:
abcdefghijklmnopqrsAvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789 _+-.,!@#$%^&*();\/|<>
12345 -98.7 3.141 .6180 9,000 +45"""

pattern3 = re.compile('[a-zA-Z0-9]+') # a부터 z까지, A부터 Z까지, 0부터 9까지 포함된 것
pattern4 = re.compile('\w+')
f = pattern3.findall(test_str)
g = pattern4.findall(test_str)
print(f)
print(g)

pattern5 = re.compile('[^a-z]+') # a부터 z까지 포함되지 않는 것.
a = pattern5.findall(test_str)
print(a)

pattern6 = re.compile('[^A-Z]+') # a부터 z까지 포함되지 않는 것.
b = pattern6.findall(test_str)
print(b)

pattern7 = re.compile('t..t') # t문자문자t ㅠㅐ턴
pattern8 = re.compile('t...t')
h = pattern7.findall(test_str)
i = pattern8.findall(test_str)
print(h)
print(i)

pattern9 = re.compile('t?est\w+') # test나 est로 시작하는 문자열 뒤에 \w가 있어야됨
pattern10 = re.compile('t?est\w*') # test나 est로 시작하는 문자열 뒤에 \w가 없어도됨
j = pattern9.findall(test_str)
k = pattern10.findall(test_str)
print(j)
print(k)