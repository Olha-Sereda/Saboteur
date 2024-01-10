import json

from flask import Flask, render_template, url_for, request, jsonify

from Game import Game
from Board import Board

app = Flask(__name__)

# PlayerList = ["Ola", "Karol", "Bugieman"]
# GameBoard = Board()
current_game = Game()


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        option = request.form['game_type']
        players_number = request.form.get("players_quantity")
        current_game.start_game(int(players_number))
        # return "Players number: "+players_number+"\n" + option
        return render_template('game.html')
    return render_template('index.html')


@app.route("/game-prestart")  # second form that is optional for now
def show():
    if request.method == "POST":
        nickname = request.form.get("nickname")
        # current_game = Game(int(players_number))
        return "Players: " + nickname + "\n"
    return render_template('prestart.html')


@app.route("/board")  # here must be board
def game():
    board_build, message = current_game.board.get_board()
    return render_template('board.html', build_board=board_build, message=message)


@app.route("/cards_in_hands")
def cards_in_hands():
    if current_game.players[current_game.current_player].move_is_ended == 0:
        your_turn_status = "Make your turn"
    else:
        your_turn_status = "Your turn is ended. Click End turn! button."
    return render_template('cards_in_hands.html',
                           player=current_game.players[current_game.current_player],
                           current_playerId=current_game.current_player, message=your_turn_status)


@app.route("/verify_move", methods=["POST"])
def verify_move():
    data = request.json
    #if isinstance()
    resp = current_game.board.verifyMove(
        current_game.players[current_game.current_player].card_in_hands[int(data["cardId"])],
        (int(data["row"]), int(data["column"])))
    # return json.dump({"response": resp})
    if resp and current_game.players[current_game.current_player].move_is_ended == 0:
        selectedCard = current_game.players[current_game.current_player].card_in_hands[int(data["cardId"])]

        # player = current_game.players[current_game.current_player]
        coords = (int(data["row"]), int(data["column"]))

        current_game.board.make_move(selectedCard, coords)
        current_game.players[current_game.current_player].move_is_ended = 1
        current_game.remove_card_in_hand(selectedCard)
    current_game.board.path_finder()
    #print(str(current_game.board.start))
    return jsonify({"response": resp})


@app.route("/verify_block_move", methods=["POST"])
def verify_block_move():
    data = request.json
    resp = current_game.verify_block_move(int(data["CardID"]), int(data["PlayerID"]))
    if resp:
        current_game.remove_card_in_hand(current_game.players[current_game.current_player].card_in_hands[int(data["CardID"])])
    return jsonify({"response": resp})


@app.route("/verify_action_move", methods=["POST"])
def verify_action_move():
    data = request.json
    resp = current_game.verify_block_move(int(data["CardID"]), int(data["PlayerID"]))
    if resp:
        current_game.remove_card_in_hand(current_game.players[current_game.current_player].card_in_hands[int(data["CardID"])])
    return jsonify({"response": resp})


@app.route("/players")
def show_players():
    return render_template('players.html', players=current_game.players, current_player=current_game.current_player)


@app.route("/action_to_player", methods=["POST"])
def action_to_player():
    # тут має накладатися еа юзера
    return True


@app.route("/end_turn")
def end_turn():
    current_game.give_one_card()
    current_game.next_turn()
    return ""


@app.route("/miss_turn", methods=["POST"])
def miss_turn():
    data = request.json
    if current_game.players[current_game.current_player].move_is_ended == 0:
        current_game.remove_card_in_hand(
            current_game.players[current_game.current_player].card_in_hands[int(data["cardId"])])
        current_game.players[current_game.current_player].move_is_ended = 1
    return ""


@app.route("/rotate_card", methods=["POST"])
def rotate_card():
    data = request.json
    print(str(data))
    current_game.players[int(data["playerId"])].card_in_hands[int(data["cardId"])].rotate()
    print(current_game.players[int(data["playerId"])].card_in_hands[int(data["cardId"])].entrances)
    return ""


@app.route("/end_game", methods=["POST"])
def end_game():
    ####pseudocode
    # if game finished successful
    # stats = current_game.show_stats()
    # return jsonify({"PropOne": stats.PropOne, "PropTwo": stats.PropTwo, ... })
    # else:
    # goto start game form
    current_game.end_game()
    # clean all current_game properties
    return ""


if __name__ == "__main__":
    app.run(debug=True)
