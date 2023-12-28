from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/game-prestart")
def show():
    return render_template('prestart.html')

@app.route("/board")
def show():
    return render_template('board.html')

if __name__ == "__main__":
    app.run(debug=True)