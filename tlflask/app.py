from flask import Flask
 
app = Flask(__name__)
 
 @app.route('/tnflask')
def tnflask():
    return 'tnflask.page '

  
