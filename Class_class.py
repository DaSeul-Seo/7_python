class charactor:
    char_cnt = 0

    def __init__(self,hp,attack,defense):
        self.info = {
            'hp':hp,
            'attack':attack,
            'defense':defense
        }

        charactor.char_cnt +=1
        print('player가 생성되었습니다. 생성된 유닛 수: %d' %(charactor.char_cnt))

player_a = charactor(10,20,30)
player_b = charactor(100,200,300)
player_c = charactor(100,200,300)

print(charactor.char_cnt)
