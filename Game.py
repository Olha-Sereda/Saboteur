from random import shuffle

from Card import Card as cd
from Card import cardList
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
        self.game_started = True
        self.players_number = players_number

        self.players = []
        for i in range(players_number):
            self.players.append(Player("Player" + str(i)))
        self.current_player = 0
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
        for i in range(self.players_number):
            for player in self.players:
                player.card_in_hands.append(self.cardStock.pop())


    #def give_one_card(self):


