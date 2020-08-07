class charactor:  # 클래스 생성
    def move(self):
        print(self, 'move')
        self.attack()

    def attack(self):
        print(self, 'attack')


player_a = charactor()  # 객체 생성
player_b = charactor()  # 객체 생성

player_a.move()
player_b.move()
