import wave
import flask
from flask import Flask, request, redirect, render_template
from flask_cors import CORS
import requests

from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': '*',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

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


@app.route("/predict", methods=["POST"])
def pred():
    file = 0
    if request.method == "POST":
        file = request.files['file'].read()
    req = requests.get("https://anotepad.com/note/read/2k9nbd2g", headers)
    soup = BeautifulSoup(req.content)
    url = soup.select_one('.plaintext').get_text()
    files = {'file': file}
    #url = "http://127.0.0.1:5500/predict"
    r = requests.post(url, data=file)

    print(r.text)
    return r.text


if __name__ == '__main__':
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    app.run()
