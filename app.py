from flask import Flask, render_template, url_for

from Board import Board

app = Flask(__name__)

PlayerList = ["Ola", "Karol"]
GameBoard = Board(PlayerList, [], 1)


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/game-restart")
def show():
    return render_template('prestart.html')


@app.route("/board")
def show():
    return render_template('board.html', build_board=GameBoard.get_board())


if __name__ == "__main__":
    app.run(debug=True)
