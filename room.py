class Room:
    def __init__(self):
        self.number_person = []

    def check_room(self, person):
        for _ in self.number_person:
            if person.chips == 1000000000:
                person.inPlay = False
            else:
                person.inPlay = True



