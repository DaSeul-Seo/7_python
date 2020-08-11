# id() 함수를 이용하면 객체의 주소를 식별할 수 있다.
# 만일 두 객체의 ID가 동일하면, 같은 객체를 참조하고 있는 것

i1 = 10
i2 = 10
print(hex(id(i1)), hex(id(i2)))
# 0x1067fb710 0x1067fb710
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(hex(id(l1)), hex(id(l2)))
# 0x106a0be88 0x106b36b08
s1 = "hello"
s2 = "hello"
print(hex(id(s1)), hex(id(s2)))
# 0x106f39110 0x106f39110
print(i1 is i2) # True
print(l1 is l2) # False
print(s1 is s2) # True