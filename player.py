class Player:
    def __init__(self):
            self.name = None
            self.password = None
            self.location = None
            self.friends = []
            self.level = 1
            self.wins = 0
            self.losses = 0
            self.draws = 0

    def register(self, name, password, location):
        self.name = name
        self.password = password
        self.location = location

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.name == other.name
        return False

    def add_friend(self, friend):
        self.friends.append(friend)

    def adjust_level(self):
        score = self.wins - self.losses
        if score == 0:
            self.level = 1
        elif 0 < score <= 5:
            self.level = 2
        elif 5 < score <= 10:
            self.level = 3
        elif score > 10:
            self.level = 4

    def add_win(self):
        self.wins += 1
        self.adjust_level()

    def add_loss(self):
        self.losses += 1
        self.adjust_level()

    def add_draw(self):
        self.draws += 1
        self.adjust_level()




    def __lt__(self, other):
        return self.level < other.level
