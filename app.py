import json

from flask import Flask, render_template, url_for, request, jsonify, redirect

from Game import Game
from Board import Board

app = Flask(__name__)

# PlayerList = ["Ola", "Karol", "Bugieman"]
# GameBoard = Board()
current_game = Game()


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        option = request.form['game_type']
        players_number = request.form.get("players_quantity")
        try:  # check if players_number is int
            if int(players_number) < 3 or int(players_number) > 10:
                return redirect(url_for('game'))
        except:
            return redirect(url_for('game'))
        current_game.start_game(int(players_number))
        return redirect(url_for('game'))
        # return "Players number: "+players_number+"\n" + option
    return render_template('index.html')


@app.route("/game")
def game():
    if not current_game.game_started:
        return redirect(url_for('home'))
    # if game round end then goto stat page
    if current_game.isRoundEnd():
        return redirect(url_for('show_stats'))

    nextTurnBtnState = ""
    if current_game.players[current_game.current_player].move_is_ended == False:
        nextTurnBtnState = "disabled"
    return render_template('game.html', nextTurnBtnVisible=nextTurnBtnState)


@app.route("/restart_game")
def restart_game():
    if (current_game.game_started and current_game.game_ended):
        current_game.restart_game()
        return redirect(url_for('game'))


@app.route("/game-prestart")  # second form that is optional for now
def show():
    if request.method == "POST":
        nickname = request.form.get("nickname")
        # current_game = Game(int(players_number))
        return "Players: " + nickname + "\n"
    return render_template('prestart.html')


@app.route("/board")  # here must be board
def board():
    board_build, message = current_game.board.get_board()
    return render_template('board.html', build_board=board_build, message=message)


@app.route("/cards_in_hands")
def cards_in_hands():
    if current_game.players[current_game.current_player].move_is_ended == False:
        your_turn_status = "Make your turn"
    else:
        your_turn_status = "Your turn is ended. Click End turn! button."
    return render_template('cards_in_hands.html',
                           player=current_game.players[current_game.current_player],
                           current_playerId=current_game.current_player, message=your_turn_status)

@app.route("/system_chat")
def system_chat():
    return render_template('system_chat.html', log_entries=current_game.messages.getLastMessages(8))

@app.route("/verify_move", methods=["POST"])
def verify_move():
    # suspend game if gold found
    if current_game.isGoldFound():
        return jsonify({"response": False, "description": "GoldFound"})
    # if game round end then goto stat page
    if current_game.isRoundEnd():
        return redirect(url_for('show_stats'))

    data = request.json
    if current_game.players[current_game.current_player].move_is_ended:
        return jsonify({"response": False, "description": "MoveAlreadyDone"})

    action_result = current_game.verify_action_move(
        current_game.players[current_game.current_player].card_in_hands[int(data["cardId"])],
        (int(data["row"]), int(data["column"])))

    if (action_result == (False, True)):
        print("Action Stole card")
        return jsonify({"response": True})

    if (action_result == (True, False)):
        print("Action View card")
        return jsonify({"response": True})

    if (not current_game.players[current_game.current_player].flag_lamp and
            not current_game.players[current_game.current_player].flag_hammer and
            not current_game.players[current_game.current_player].flag_truck):
        #print("Path card")
        resp = current_game.board.verifyMove(
            current_game.players[current_game.current_player].card_in_hands[int(data["cardId"])],
            (int(data["row"]), int(data["column"])))
        # return json.dump({"response": resp})
        if resp and current_game.players[current_game.current_player].move_is_ended == False:
            selectedCard = current_game.players[current_game.current_player].card_in_hands[int(data["cardId"])]

            # player = current_game.players[current_game.current_player]
            coords = (int(data["row"]), int(data["column"]))

            current_game.board.make_move(selectedCard, coords)
            current_game.players[current_game.current_player].move_is_ended = True
            current_game.remove_card_in_hand(selectedCard)

        # тут перевірка шляху та відкриття фінішних карт
        if current_game.board.path_finder() == 2:
            current_game.gold_founded = True

        # Тут виклик кінця гри і статистики
        # print(str(current_game.board.start))
        desc = ""
        if resp:
            desc = "AcceptedMove"
        else:
            desc = "WrongMove"
        return jsonify({"response": resp, "description": desc})
    return jsonify({"response": False, "description": "UserUnderBlockCard"})


@app.route("/verify_block_move", methods=["POST"])
def verify_block_move():
    # suspend game if gold found
    if current_game.isGoldFound():
        return jsonify({"response": False, "description": "GoldFound"})
    # if game round end then goto stat page
    if current_game.isRoundEnd():
        return redirect(url_for('show_stats'))

    data = request.json
    resp = False
    if not current_game.players[current_game.current_player].move_is_ended:
        resp = current_game.verify_block_move(int(data["CardID"]), int(data["PlayerID"]))
        if resp:
            current_game.remove_card_in_hand(
                current_game.players[current_game.current_player].card_in_hands[int(data["CardID"])])
            current_game.players[current_game.current_player].move_is_ended = True
        else:
            resp = False
    return jsonify({"response": resp, "description": "WrongMove"})


@app.route("/players")
def show_players():
    return render_template('players.html', players=current_game.players, current_player=current_game.current_player)


@app.route("/end_turn")
def end_turn():
    if current_game.isGoldFound():
        return jsonify({"response": False, "description": "GoldFound"})
    # if game round end then goto stat page
    if current_game.isRoundEnd():
        return redirect(url_for('show_stats'))

    current_game.give_one_card()
    current_game.next_turn()
    return ""


@app.route("/miss_turn", methods=["POST"])
def miss_turn():
    # suspend game if gold found
    if current_game.isGoldFound():
        return jsonify({"response": False, "description": "GoldFound"})
    # if game round end then goto stat page
    if current_game.isRoundEnd():
        return redirect(url_for('show_stats'))

    data = request.json
    if not current_game.players[current_game.current_player].move_is_ended:
        current_game.remove_card_in_hand(
            current_game.players[current_game.current_player].card_in_hands[int(data["cardId"])])
        current_game.players[current_game.current_player].move_is_ended = True
    return jsonify({"response": current_game.players[current_game.current_player].move_is_ended})


@app.route("/rotate_card", methods=["POST"])
def rotate_card():
    data = request.json
    current_game.players[int(data["playerId"])].card_in_hands[int(data["cardId"])].rotate()
    return ""


@app.route("/end_game_round")
def end_game_round():
    current_game.end_game_round()
    # calculate statistic data
    current_game.calculate_stats()
    ######
    return redirect(url_for('show_stats'))


@app.route("/show_stats")
def show_stats():
    if not current_game.game_started:
        return redirect(url_for('home'))
    if not current_game.game_ended:
        return redirect(url_for('game'))

    board_build, message = current_game.board.get_board()
    return render_template('statistic.html',
                           players=current_game.players,
                           current_player=current_game.current_player,
                           build_board=board_build)


@app.route("/end_game")
def end_game():
    # clean all current_game properties
    current_game.end_game()
    return redirect(url_for('home'))


@app.route("/connection", methods=["POST"])
def connection():
    return "Connected"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=12140)
