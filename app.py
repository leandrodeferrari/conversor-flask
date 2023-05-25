from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/conversor", methods=["POST"])
def conversor():
    return "Convertir"

app.run(host= "0.0.0.0", port= 3000, debug= True)