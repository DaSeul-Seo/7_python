class charactor:

    def __init__(self, hp):
        self.hp = hp
        print('player가 생성되었습니다.')

    def __call__(self):
        print('hp: %d' %(self.hp))

player_a = charactor(10)
player_b = charactor(100)

print(player_a.hp)
print(player_b.hp)
