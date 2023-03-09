from flask import Flask, render_template, request
import json

app = Flask(__name__)

liste = []

steder= []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        steder = request.form["steder"]
        liste.append(steder)
    return render_template("index.html", liste=liste)

@app.route("/hoteller")
def hoteller():
    fil=open("hoteller.json")
    data=json.load(fil)
    fil.close()
    return render_template("hoteller.html", data=data)

@app.route("/steder")
def steder():
    fil=open("steder.json")
    data=json.load(fil)
    fil.close()
    return render_template("steder.html", data=data)

@app.route("/steder/slett/<id>")
def rute_slett(id):
    steder.remove(id)
    return steder()

app.run(debug=True)