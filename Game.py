from random import shuffle

from Card import Card as cd
from Card import cardList, BlockCard, PathCard, ActionCard, FinishCard, blank_card, isinstanceCard
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
        self.game_ended = False

    def start_game(self, players_number: int):
        if self.game_started == False:
            self.board = Board()
            self.game_started = True
            self.players_number = players_number

            self.players = []
            for i in range(players_number):
                self.players.append(Player("Player" + str(i)))
            self.current_player = 0
            #self.players[0].flag_hammer = True
            #self.players[0].flag_lamp = True
            #self.players[0].flag_truck = True
            self.board.arr[2][1] = PathCard(10, "1111_full.png", (1, 1, 1, 1))
            self.board.arr[2][2] = PathCard(11, "1111_full.png", (1, 1, 1, 1))
            self.board.arr[2][3] = PathCard(12, "1111_full.png", (1, 1, 1, 1))
            self.board.arr[2][4] = PathCard(13, "1111_full.png", (1, 1, 1, 1))
            self.board.arr[2][5] = PathCard(14, "1111_full.png", (1, 1, 1, 1))
            self.board.arr[2][6] = PathCard(10, "1111_full.png", (1, 1, 1, 1))

            self.cardStock = cardList.copy()
            shuffle(self.cardStock)
            if self.players_number >= 3 and self.players_number <= 5:
                self.initialCardNumber = 6
            elif self.players_number >=6 and self.players_number <=7:
                self.initialCardNumber = 5
            else:
                self.initialCardNumber = 4

            self.initial_give_cards()

    def restart_game(self):
        if self.game_started == True and self.game_ended == True:
            self.game_ended = False
            self.current_player = 0
            self.cardStock = cardList.copy()
            shuffle(self.cardStock)
            self.board = Board()
            for player in self.players:
                player.flag_lamp = False
                player.flag_truck = False
                player.flag_hammer = False
                player.card_in_hands=[]
            self.initial_give_cards()

    def initial_give_cards(self):
        for i in range(self.initialCardNumber):
            for player in self.players:
                player.card_in_hands.append(self.cardStock.pop())

        #self.players[0].card_in_hands.append(cardList[28])

    def remove_card_in_hand(self, selectedCard):
        self.players[self.current_player].card_in_hands.remove(selectedCard)

    def put_blockcard_on_player(self, selectedCard, player: int):
        if isinstanceCard(selectedCard, "BlockCard"):
            if selectedCard.type_card == "Lamp" and selectedCard.block == True:
                self.players[player].add_lamp()
            if selectedCard.type_card == "Lamp" and selectedCard.block == False:
                self.players[player].del_lamp() #треба перевірити чи людина була до того заблокованаб інакше ход не повинен відбутися
        player.card_in_hands.remove(selectedCard)

    def next_turn(self):
        self.current_player += 1
        if self.current_player >= self.players_number:
            self.current_player = 0
        self.players[self.current_player].move_is_ended = False
        self.board.close_finish_cards()

    def give_one_card(self):
        if len(self.cardStock) > 0:
            self.players[self.current_player].card_in_hands.append(self.cardStock.pop())

    def return_to_game(self):
        self.game_ended = False

    def end_game_round(self):
        # Calculate statistics and create or update the object with total amount data
        self.game_ended = True
        #return Stat object

    def end_game(self):
        self.initialCardNumber = None
        self.cardStock = None
        self.current_player = None
        self.players = None
        self.board = Board()
        self.players_number = None
        self.game_started = False
        self.game_ended = False

    def verify_block_move(self, CardID: int, PlayerID: int):
        BlockFlag = False
        UnBlockFlag = False
        Player = self.players[PlayerID]
        Card = self.players[self.current_player].card_in_hands[CardID]
        if isinstanceCard(Card, "BlockCard") and Card.block:
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

        if isinstanceCard(Card, "BlockCard") and Card.block == False:
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

    def verify_action_move(self, card: ActionCard, BoardCoords: tuple):
        if isinstanceCard(card, "ActionCard"):
            if card.type_card == "StoleCard" and isinstanceCard(self.board.arr[BoardCoords[0]][BoardCoords[1]], "PathCard") and BoardCoords != (2, 0):
                self.board.arr[BoardCoords[0]][BoardCoords[1]] = blank_card
                self.players[self.current_player].move_is_ended = True
                self.remove_card_in_hand(card)
                return True, False
            if card.type_card == "ViewGold" and isinstanceCard(self.board.arr[BoardCoords[0]][BoardCoords[1]], "FinishCard"):
                self.board.arr[BoardCoords[0]][BoardCoords[1]].temporary_show = True
                self.players[self.current_player].move_is_ended = True
                self.remove_card_in_hand(card)
                return False, True
        return False, False