class unit:
    unit_count = 0

    def __init__(self):
        print('unit생성')
        unit.unit_count +=1

    def move(self):
        print('unit move')

class bird(unit):
    def __init__(self):
        print('bird생성')
        super(bird, self).__init__()

b1 = bird()
b3 = bird()

b1.move()

# g1 = ground()

print(unit.unit_count)
