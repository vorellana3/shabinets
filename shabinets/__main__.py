from flask import Flask

app = Flask("shabinets")

@app.route('/')

def hello():

    return "Hello world!"