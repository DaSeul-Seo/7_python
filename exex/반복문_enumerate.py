# 요소의 값은 물론 인덱스가 필요할 경우 enumerage() 함수를 이용

colors = ['red', 'orange', 'yellow', 'green', 'pink', 'blue']
for index, color in enumerate(colors):
    print(index, color)
    # 0 red
    # 1 orange
    # 2 yellow
    # 3 green
    # 4 pink
    # 5 blue