# enumerate
# 순차 자료형에서 현재 아이템의 색인과 함께 처리하고자 할 때 흔히 사용

i = 0
for value in ['red', 'yellow', 'blue', 'white', 'grey']:
    print('{0}: {1}'.format(i, value))
    i += 1
    # 0: red
    # 1: yellow
    # 2: blue
    # 3: white
    # 4: grey
# 비교 : enumerate 함수를 사용했을 때
for i, value in enumerate(['red', 'yellow', 'blue', 'white', 'grey']):
    print('{0}: {1}'.format(i, value))
    # 0: red
    # 1: yellow
    # 2: blue
    # 3: white
    # 4: grey