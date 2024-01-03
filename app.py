from flask import Flask, render_template, url_for, request

from Board import Board

app = Flask(__name__)

PlayerList = ["Ola", "Karol"]
GameBoard = Board(PlayerList, [], 1)


@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        option = request.form['game_type']
        players_number = request.form.get("players_quantity")
        return "Players number: "+players_number+"\n" + option
    return render_template('index.html')


@app.route("/game-restart")
def show():
    return render_template('prestart.html')


@app.route("/board")
def game():
    return render_template('board.html', build_board=GameBoard.get_board())


if __name__ == "__main__":
    app.run(debug=True)
