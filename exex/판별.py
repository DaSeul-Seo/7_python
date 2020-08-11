# isdigit() : 문자열이 숫자로 구성되어 있는가 여부를 반환
# isalpha() : 문자열이 알파벳으로 구성되어 있는가 여부를 반환
# islower() : 문자열이 소문자로 구성되어 있는가 여부를 반환
# isupper() : 문자열이 대문자로 구성되어 있는가 여부를 반환
# isspace() : 문자열이 공백문자로 구성되어 이쓴ㄴ가 여부를 반환

print('1234'.isdigit()) # True
print('abcd'.isalpha()) # True

print('1234'.isalpha()) # False
print('abcd'.isdigit()) # False

print('abcd'.islower()) # True
print('ABCD'.isupper()) # True

print('\n\n'.isspace()) # True
print(' '.isspace()) # True
print(''.isspace()) # False