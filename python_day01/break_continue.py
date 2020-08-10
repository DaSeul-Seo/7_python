# break는 해당 반복문을 완전 탈출하라는 의미
# continue를 만나면 그 아래의 코드는 실행이 되지 않고 다음 번 요소실행.
# while이라면 다시 검사하는 부분으로 이동

# break
for i in range(0,10):
    print(i)
    break # 해당 반복문 탈출
    print('test') # break때문에 실행되기 전 탈출

print()

# continue
for i in range(0,10):
    print(i)
    continue # 아래는 실행하지 않고 다음번 반복 실행
    print('test') # continue 때문에 실행되지 않음

