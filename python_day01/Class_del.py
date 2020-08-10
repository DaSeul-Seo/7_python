class charactor:

    def __init__(self, hp, attack, defense):
        pass

    def __del__(self):
        print('player가 죽었습니다.')

player_a = charactor(10,20,30)
player_b = charactor(100,200,300)
player_c = charactor(100,200,300)

del player_a # player가 죽었습니다.
del player_b # player가 죽었습니다.
del player_c # player가 죽었습니다.
