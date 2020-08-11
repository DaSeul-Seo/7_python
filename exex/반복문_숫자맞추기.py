import random

randNumber = random.randint(1,100) # 1-100 난수 발생
count = 0

while True :
    inputNumber = int(input("숫자를 입력하세요"))
    count +=1
    if randNumber == inputNumber : # 정답이면 break
        break
    elif randNumber > inputNumber :
        print(inputNumber, "보다 큽니다")
    else :
        print(inputNumber, "보다 작습니다.")

print(count, "번만에 정답을 맞추었습니다.")
