import json

from flask import Flask, render_template, url_for, request, jsonify

from Game import Game
from Board import Board

app = Flask(__name__)

PlayerList = ["Ola", "Karol"]
GameBoard = Board()
current_game = Game()


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        option = request.form['game_type']
        players_number = request.form.get("players_quantity")
        current_game.start_game(int(players_number))
        #return "Players number: "+players_number+"\n" + option
        return render_template('game.html')
    return render_template('index.html')


@app.route("/game-prestart") #second form that is optional for now
def show():
    if request.method == "POST":
        nickname = request.form.get("nickname")
        #current_game = Game(int(players_number))
        return "Players: "+nickname+"\n"
    return render_template('prestart.html')


@app.route("/board")  # here must be board
def game():
    board_build, message = current_game.board.get_board()
    return render_template('board.html', build_board=board_build, message=message)


@app.route("/cards_in_hands")
def cards_in_hands():
    return render_template('cards_in_hands.html', player=current_game.players[current_game.current_player])


@app.route("/verify_move", methods=["POST"])
def verify_move():
    data = request.json
    resp = current_game.board.verifyMove(current_game.players[current_game.current_player].card_in_hands[data["cardId"]], (int(data["row"]), int(data["column"])))
    #return json.dump({"response": resp})
    if resp == True:
        selectedCard = current_game.players[current_game.current_player].card_in_hands[data["cardId"]]
        #player = current_game.players[current_game.current_player]
        coords = (int(data["row"]), int(data["column"]))

        current_game.board.make_move(selectedCard, coords)
        current_game.remove_card_in_hand(selectedCard)
    print(str(current_game.board.start))
    return jsonify({"response": resp})


@app.route("/players")
def show_players():
    return render_template('players.html', players=current_game.players)


@app.route("/action_to_player", methods=["POST"])
def action_to_player():
    #тут має накладатися еа юзера
    return True




if __name__ == "__main__":
    app.run(debug=True)
