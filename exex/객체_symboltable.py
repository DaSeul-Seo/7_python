# 파이썬에서 모든 자료(데이터)들은 객체의 형태로 저장된다.
# 파이썬의 변수는 컴파일러 언어처럼 변수에 할당된 값을 저장하는 저장공간(메모리)의 주소 심볼릭이 아니다.
# 변수는 단지 객체의 이름(심볼)일 뿐이다.
# 파이썬의 객체 이름(변수)과 객체의 ID(주소)는 심볼 테이블에 함께 저장되어 관계를 갖게 된다.

# <심볼테이블>
# 변수의 이름과 저장된 데이터의 주소를 저장하는 테이블
# 심볼테이블의 내용을 살펴보기 위해 globals(), locals()내장함수 이용
# 두 함수는 해당 스코프 내 심볼 테이블의 내용을 dict타입의 객체로 반환

# 글로벌 변수 선언
g_a = 1
g_b = "symbol"
# 로컬 변수 확인을 위한 함수 선언
def f():
    l_a = 2
    l_b = "table"
    # 로컬 심볼테이블 확인
    print(locals())

f()
# {'l_a': 2, 'l_b': 'table'}

globals()