# %s : 문자열(string)
# %c : 문자 1개(character)
# %d : 정수(integer)
# %f : 부동소수(floating point)
# %o : 8진수
# %x : 16진수
# %% : Literal%

a = "I have %d apples" %5
b = "interest rate is %2.4f" % 1.24
c = "interest rate is %f" % 1.240

print(a) # I have 5 apples
print(b) # interest rate is 1.2400
print(c) # interest rate is 1.240000
