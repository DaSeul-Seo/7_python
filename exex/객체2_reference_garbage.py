# 레퍼런스 카운트와 쓰레기 수집
# 레퍼런스 카운트(Reference Count) : 객체를 참조하는 참조 수
# 레퍼런스 카운트가 0이 되면 사용하지 않는 객체로 판단, 자동으로 사라짐
# 이러한 작업을 쓰레기 수집(Garbage Collection)

import sys
x = object()
sys.getrefcount(x)
2
y = x
sys.getrefcount(x)
3
sys.getrefcount(y)
3
del(x) # 레퍼런스 값이 줄어든다
sys.getrefcount(y)
2