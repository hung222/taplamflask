

from flask import Flask
app = Flask("my website")

 @app.route("/")
 def giachoi():
   return "giachoi"

 @app.route("/giachoi/<string:name>")
 def giachoi(name):
    return "giachoi {}".format(name)

@app.route("tnflask/")
 def tnflask():
    return "tnflask.html"



 

