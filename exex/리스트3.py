# Stack과 Queue 사용
# Stack = Last in, first out
# Queue = First in, first out

stack = [ ]
stack.append(10)
stack.append(20)
stack.append(30)
print(stack) # [10, 20, 30]
print(stack.pop()) # 30 # 마지막 인덱스 버림
print(stack.pop()) # 20
print(stack) #[10]

queue = [ ]
queue.append(100)
queue.append(200)
queue.append(300)
print(queue) # [100, 200, 300]
print(queue.pop(0)) # 가장 앞쪽 인덱스의 요소를 pop # 100
print(queue.pop(0)) # 200
print(queue) # [300]