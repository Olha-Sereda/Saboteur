from flask import Flask, render_template, url_for, request

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
    board_build, message = GameBoard.get_board()
    return render_template('board.html', build_board=board_build, message=message)


@app.route("/cards_in_hands")
def cards_in_hands():
    return render_template('cards_in_hands.html', player=current_game.players[current_game.current_player])


if __name__ == "__main__":
    app.run(debug=True)
