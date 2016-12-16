from flask import Flask, app, request, session, flash


# export FLASK_APP=main.py
# python3 -m flask run


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/hello', methods=['GET'])
def login():
    return 'Zhan, you are awesome!!!'
