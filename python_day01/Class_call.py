class charactor:

    def __init__(self, hp):
        self.hp = hp
        print('player가 생성되었습니다.')

    def __call__(self):
        print('hp: %d' %(self.hp))

player_a = charactor(10)
player_b = charactor(100)

player_a() # hp:10
player_b() # hp:100

print(callable(player_a)) # 실행 가능한지 판별 (call이라는 메소드가 정의되어있나 안되어있나)
