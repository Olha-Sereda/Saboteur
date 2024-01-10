from random import shuffle

from Card import Card as cd
from Card import cardList, BlockCard
from Player import Player
from Board import Board


class Game:
    def __init__(self):
        self.initialCardNumber = None
        self.cardStock = None
        self.current_player = None
        self.players = None
        self.board = Board()
        self.players_number = None
        self.game_started = False

    def start_game(self, players_number: int):
        if self.game_started == False:

            self.game_started = True
            self.players_number = players_number

            self.players = []
            for i in range(players_number):
                self.players.append(Player("Player" + str(i)))
            self.current_player = 0
            self.players[0].flag_hammer = True
            self.players[0].flag_lamp = True
            self.players[0].flag_truck = True
            self.cardStock = cardList.copy()
            shuffle(self.cardStock)
            if self.players_number >= 3 and self.players_number <= 5:
                self.initialCardNumber = 6
            elif self.players_number >=6 and self.players_number <=7:
                self.initialCardNumber = 5
            else:
                self.initialCardNumber = 4

            self.initial_give_cards()

    def initial_give_cards(self):
        for i in range(self.initialCardNumber):
            for player in self.players:
                player.card_in_hands.append(self.cardStock.pop())

        #self.players[0].card_in_hands.append(cardList[28])

    def remove_card_in_hand(self, selectedCard):
        self.players[self.current_player].card_in_hands.remove(selectedCard)

    def put_blockcard_on_player(self, selectedCard, player: int):
        if isinstance(selectedCard, BlockCard):
            if selectedCard.type_card == "Lamp" and selectedCard.block == True:
                self.players[player].add_lamp()
            if selectedCard.type_card == "Lamp" and selectedCard.block == False:
                self.players[player].del_lamp() #треба перевірити чи людина була до того заблокованаб інакше ход не повинен відбутися
        player.card_in_hands.remove(selectedCard)

    def next_turn(self):
        self.current_player += 1
        if self.current_player >= self.players_number:
            self.current_player = 0
        self.players[self.current_player].move_is_ended = 0

    def give_one_card(self):
        if len(self.cardStock) > 0:
            self.players[self.current_player].card_in_hands.append(self.cardStock.pop())


    def end_game(self):
        self.game_started = False


    def verify_block_move(self, CardID: int, PlayerID: int):
        BlockFlag = False
        UnBlockFlag = False
        Player = self.players[PlayerID]
        Card = self.players[self.current_player].card_in_hands[CardID]
        if isinstance(Card, BlockCard) and Card.block:
            if Card.type_card == "Lamp" and Player.flag_lamp == False:
                Player.add_lamp()
                BlockFlag = True
            if Card.type_card == "Truck" and Player.flag_truck == False:
                Player.add_truck()
                BlockFlag = True
            if Card.type_card == "Hammer" and Player.flag_hammer == False:
                Player.add_hammer()
                BlockFlag = True
            return BlockFlag

        if isinstance(Card, BlockCard) and Card.block == False:
            if Card.type_card == "Lamp" and Player.flag_lamp == True:
                Player.del_lamp()
                UnBlockFlag = True
            if Card.type_card == "Truck" and Player.flag_truck == True:
                Player.del_truck()
                UnBlockFlag = True
            if Card.type_card == "Hammer" and Player.flag_hammer == True:
                Player.del_hammer()
                UnBlockFlag = True
            return UnBlockFlag

        return False

    def verify_action_move(self):
        return True