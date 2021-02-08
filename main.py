import wave
from flask import Flask, request, redirect, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/clients")
def mod():
    return render_template('clients.html')


@app.route("/more")
def about():
    return render_template('more.html')


@app.route("/Afile", methods=['POST'])
def afile():
    blob = request.files['file'].read()
    with open('myfile.wav', mode='wb') as f:
        f.write(blob)
    from flask import jsonify
    resp = jsonify(success=True)
    return resp


app.config["TEMPLATES_AUTO_RELOAD"] = True


if __name__ == '__main__':
    app.run()
