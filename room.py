class Room:
    def __init__(self):
        self.number_person = []

    def check_room(self, person):
        for person in self.number_person:
            if person.chips <= 100000:
                person.inPlay = False
            else:
                person.inPlay = True



