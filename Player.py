class Player:
    def __init__(self, flag_lamp: bool, flag_truck: bool, flag_hammer: bool, card_in_hands: list):
        self.flag_lamp = flag_lamp
        self.flag_truck = flag_truck
        self.flag_hammer = flag_hammer
        self.card_in_hands = card_in_hands