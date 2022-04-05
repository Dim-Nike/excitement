class Person:
    def __init__(self, name, chips, room):
        self.name = name
        self.chips = chips
        self.room = room
        self.bid = 0
        self.card = ''
        self.inPlay = True
        self.card = {}
        self.count_card = 2

    def up_ante(self, count):
        self.bid = count
        self.chips -= count

    def skip(self):
        self.bid = 0

    def throw_off(self):
        self.inPlay = False

    def get_card(self, two_card):
        print(f'Я {self.name} у меня карты: {two_card}')

    def __str__(self):
        return f'I am {self.name}'





