# >리스트와 거의 비슷하지만 다름 : 시퀀스 자료형
#  - 튜플은 ()기호로 생성하며 그 값을 바꿀 수 없다(immutable)
#  - 하나의 요소만을 가질 때는 요소 뒤에 콤마(,)를 반드시 붙임
#  - 괄호를 생략해도 튜플로 인식

t = (1, 2, 3)
print(t, type(t)) # (1, 2, 3) <class 'tuple'>
t = 1, 2, 'python' # ( )를 생략해도 튜플을 생성할 수 있다
print(t, type(t)) # (1, 2, 'python') <class 'tuple'>
print(t[-2], t[-1], t[0], t[1], t[2]) # 인덱싱 # 2 python 1 2 python
print(t[1:3]) # 슬라이싱 # (2, 'python')
print(t[:]) # (1, 2, 'python')
print(t * 2) # 반복(*) # (1, 2, 'python', 1, 2, 'python')
print(t + (3, 4, 5)) # 연결(+) # (1, 2, 'python', 3, 4, 5)
print(len(t)) # 요소 개수 반환 # 3
print(5 in t) # 요소 5가 내부에 있는지 확인 # False