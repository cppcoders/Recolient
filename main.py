import wave
from flask import Flask, request, redirect, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/clients")
def mod():
    return render_template('clients.html')


@app.route("/more")
def about():
    return render_template('more.html')


if __name__ == '__main__':
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    app.run(port=5200)
