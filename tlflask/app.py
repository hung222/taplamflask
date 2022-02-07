from flask import Flask
 
app = Flask(__name__)
 
 
@app.route('/')
def trangchu():
    return 'trangchu'

@app.route('/tnflask')
def tnflask():
    return 'tnflask.page '

  