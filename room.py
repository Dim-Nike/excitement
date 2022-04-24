class Room:
    def __init__(self):
        self.number_person = []

    def check_room(self, list_users):
        for user in list_users:
            if user.chips <= 0:
                user.inPlay = False
            else:
                user.inPlay = True



