from flask import Flask, render_template, url_for, request

from Game import Game
from Board import Board

app = Flask(__name__)

PlayerList = ["Ola", "Karol"]
GameBoard = Board()



@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        option = request.form['game_type']
        players_number = request.form.get("players_quantity")
        current_game = Game(int(players_number))
        #return "Players number: "+players_number+"\n" + option
        return str(type(current_game))
        #return render_template('board.html', build_board=current_game.board.get_board(), message=current_game.board.start)
    return render_template('index.html')


@app.route("/game-restart")
def show():
    if request.method == "POST":
        nickname = request.form.get("nickname")
        #current_game = Game(int(players_number))
        return "Players: "+nickname+"\n"
    return render_template('prestart.html')


@app.route("/board")
def game():
    board_build, message = GameBoard.get_board()

    return render_template('board.html', build_board=board_build, message=message)


if __name__ == "__main__":
    app.run(debug=True)
