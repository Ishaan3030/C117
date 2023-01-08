from flask import Flask,render_template, url_for,request,jsonify
from text_sentiment_prediction import *

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict_emotion', methods=['POST'])
def predict_emotion():

    if not input_text:

app.run(debug = True)


    