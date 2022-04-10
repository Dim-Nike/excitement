class Chips:
    def __init__(self, room=True):
        self.room = room
        self.total_bank = 0
        self.points = []

    def win_check(self, point, room, user):
        self.points.append(point)
        highest_score = 0
        if len(self.points) == len(room.number_person):
            highest_score = max(self.points)
            print(f'---Наивысший балл - {highest_score}---')
        if len(self.points) == len(room.number_person) and highest_score == point:
            user.chips += self.total_bank
            print(f'Фишки передаются игроку с наивысшим баллом - {point}\n'
                  f'Количество фишек - {self.total_bank}')
            self.total_bank = 0





