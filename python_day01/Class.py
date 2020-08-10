class charactor: # 클래스 생성
    def move(self):
        print('move')
        
    def attack(self):
        print('attach')
        
player_a = charactor() # 객체 생성
player_b = charactor() # 객체 생성

player_a.move() # move 출력
player_a.attack()
player_b.move()
player_b.attack() # attack 출력
