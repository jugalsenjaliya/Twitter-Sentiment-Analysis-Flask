# source venv/bin/activate

from flask import Flask, render_template, request

# from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

import nltk
nltk.download('vader_lexicon')

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def man():
    if request.method == "POST":
        inp = request.form.get("inp")
        # sid = SentimentIntensityAnalyzer()
        # score = sid.polarity_scores(inp)
        analysis = TextBlob(inp)
        if analysis.sentiment.polarity > 0:
            return render_template('home2.html',message="Positive")
        elif analysis.sentiment.polarity == 0:
            return render_template('home2.html',message="Neutral")
        else:
            return render_template('home2.html',message="Negative")
    return render_template('home2.html')


if __name__ == '__main__':
    app.debug = True
    app.run()




# from flask import Flask,render_template,url_for,request
# import pandas as pd 
# import pickle
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.naive_bayes import MultinomialNB
# import joblib
# import pickle

# # load the model from disk
# filename = 'nlp_model2.pkl'
# clf = pickle.load(open(filename, 'rb'))
# cv=pickle.load(open('tranform2.pkl','rb'))
# app = Flask(__name__)

# @app.route('/', methods=["GET", "POST"])
# def main():
# 	if request.method == 'POST':
# 		message = request.form['message']
# 		data = [message]
# 		vect = cv.transform(data)
# 		my_prediction = clf.predict(vect)
# 		if my_prediction==1:
# 			return render_template('home3.html',prediction = "Positive")
# 		else:
# 			return render_template('home3.html',prediction = "Negative")
# 	return render_template('home3.html')
