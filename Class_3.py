class charactor:

    def __init__(self, hp, attack, defense):
        self.hp = hp
        self.attack = attack
        self.defense = defense
        print('player가 생성되었습니다.')

    def create(self, hp, attack, defense):
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def move(self):
        print(self, 'move')
        self.attack()

    def attack(self):
        print(self, 'attack')

    def show_info(self):
        print("hp: %d, attack: %d, defense: %d" %(self.hp, self.attack, self.defense))

player_a = charactor()
player_b = charactor()

player_a.create(10,20,30)
player_b.create(100,200,300)

player_a.show_info() # hp:10, attack:20, defense:30
player_b.show_info() # hp:100, attack:200, defense:300
