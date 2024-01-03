class Player:
    def __init__(self, nickname: str):
        self.nickname = nickname
        self.flag_lamp = 0
        self.flag_truck = 0
        self.flag_hammer = 0
        self.card_in_hands = []