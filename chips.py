class Chips:
    def __init__(self, room=True):
        self.room = room
        self.total_bank = 0
        self.points = []
        self.highest_score = 0
        self.number_of_wins = 0
        self.max_bid = 0
        self.users_wins = []

    def check_win(self, room):
        for user in room.number_person:
            self.points.append(user.points)

        score_max = max(self.points)
        print(f'Всего баллов - {self.points}')
        print(f'Наивысший балл - {score_max}')

        for win_user in room.number_person:
            if score_max <= win_user.points:
                self.users_wins.append(win_user)
        print(f'Всего победителей - {len(self.users_wins)}')

        for user in self.users_wins:
            user.chips += self.total_bank // len(self.users_wins)
            print(f'{user.name} получил {self.total_bank // len(self.users_wins)} фишек!')

    def bid_check(self, user, number_person, happening=1, higher_rate_user=0):
        highest_bid = 0
        for playing in number_person:
            if playing.bid > highest_bid:
                highest_bid = playing.bid
        print(f'Наивысшая ставка - {highest_bid}')
        if happening == 0:
            return highest_bid
        if happening == 1:
            if highest_bid == user.bid:
                return True
        if happening == 2:
            if higher_rate_user >= highest_bid:
                return True
        if happening == 3:
            if user.bid > highest_bid:
                return True
        if happening == 4:
            if user.chips <= highest_bid:
                return True

    def remove_values(self):
        self.highest_score = 0
        self.total_bank = 0
        self.number_of_wins = 0
        self.points = []
        self.users_wins = []






