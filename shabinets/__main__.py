from flask import Flask

app = Flask("shabinets")

@app.route('/hello')

def hello():

    return "Hello world!"

