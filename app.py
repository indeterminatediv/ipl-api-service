from flask import Flask
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"

app.run(debug = True)
