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


@app.route("/getfile")
def getfile():
    from flask import send_file
    path_to_file = "myfile.wav"

    return send_file(
        path_to_file,
        mimetype="audio/wav",
        as_attachment=True,
        attachment_filename="test.wav")


@app.route("/Afile", methods=['POST'])
def afile():
    blob = request.files['file'].read()
    with open('myfile.wav', mode='wb') as f:
        f.write(blob)
    from flask import jsonify
    resp = jsonify(success=True)
    return resp


if __name__ == '__main__':
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    app.run()
