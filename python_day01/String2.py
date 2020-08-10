var="hello world"
print(var[0])
print()

# 문자열 나누기
var1="hello world !@"
print(var.split()) #['hello', 'world', '!@']
print()

# 대/소문자 변환
var2="hello world"
var3="HELLO WORLD"
print(var2.upper())
print(var3.lower())
print()

# 문자력길이 구하기

# 공백제거
var4="   hello world   "
print(var4.rsplit()) # 우측 공백제거
print(var4.lstrip()) # 좌측 공백제거
print(var4.strip()) # 양측 공백제거

# 포맷팅
var5 = 'I am' + '홍길동'
print(var5) # I am 홍길동
var6 = "I am {name}".format(name="홍길동")
print(var6) # I am 홍길동
var7 = "I am {0}".format("홍길동")
print(var7) # I am 홍길동
var8 = "I am {0} I am {name}".format("홍길동", name="정보문화사")
print(var8) # I am 홍길동 출력 I am 정보문화사
