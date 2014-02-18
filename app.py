from flask import Flask
from minnows import minnows
from fish import fish
from sharks import sharks

app = Flask(__name__)

app.register_blueprint(minnows, url_prefix='/minnows')
app.register_blueprint(fish, url_prefix='/fish')
app.register_blueprint(sharks, url_prefix='/sharks')

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
