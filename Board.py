class Board:
    def __init__(self, players: list, card_stock: list, arr: list, current_player: int):
        self.players = players
        self.card_stock = card_stock
        self.arr = arr
        self.current_player = current_player

    def give_card_to_player(self, current_player: int):
        if len(self.card_stock) > 0:
            card = self.card_stock.pop()
            self.players[current_player].card_in_hands.append(card)
            print(f"Player {current_player} received card {card}.")
        else:
            print("No more cards in the stock.")