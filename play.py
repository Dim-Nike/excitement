class Person:
    def __init__(self, name, chips, room, ):
        self.name = name
        self.chips = chips
        self.room = room
        self.bid = 0
        self.card = ''
        self.inPlay = True

    def up_ante(self, count):
        self.bid = count
        self.chips -= count

    def skip(self):
        self.bid = 0

    def throw_off(self):
        self.inPlay = False
