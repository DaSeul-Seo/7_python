# range
# range({start = 0,} end {, step = 1})
# start부터 end까지의 순차적 리스트를 step 간격으로 생성

seq = range(10) # 0이상 10 미만의 순차적 정수 목록
print(seq, type(seq)) # range(0, 10) <class 'range'>
print(seq[0:]) # range(0, 10)
print(len(seq)) # 10
for i in seq:
    print(i) # 0/1/2/3/4/5/6/7/8/9
    seq2 = range(5, 15) # 5 이상 15 미만의 순차적 정수 목록
for i in seq2:
    print(i) # 5/6/7/8/9/10/11/12/13/14
    seq3 = range(0, -10, -1) # 0 이하 -10 초과의 순차적 정수 목록
for i in seq3:
    print(i) # 0/-1/-2/-3/-4/-5/-6/-7/-8/-9