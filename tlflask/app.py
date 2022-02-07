from flask import Flask
app = Flask(__name__)

@app.route("tnflask.html/")
def tnflask.html():
    return "tnflask.html"
