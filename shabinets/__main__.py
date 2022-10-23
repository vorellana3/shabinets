from flask import Flask, jsonify
import json

app = Flask("shabinets")

@app.route('/')


def index():

    return jsonify({'1': 'sugar',
                    '2': 'milk'})

app.run()
