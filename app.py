from flask import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB , GaussianNB
from pickle import load

import pandas as pd
import numpy as np


app = Flask(__name__)

def preprocess_data(data):
	data = data.replace('\d+',' ')
	data = data.replace('[^a-zA-Z0-9 \n]', ' ')
	return data

@app.route('/',methods = ['GET', 'POST'])
def homepage():
	data = request.args.get('data')
	if not data:
		return jsonify(success = 0)

	data = preprocess_data(data)
	
	df = pd.DataFrame({'Message':data})
	print df
	
	vect = load(file('vect.dat'))
	model = load(file('model.dat'))
	
	result = model.predict(vect.transform(df))
	print result
	
	return jsonify(spam = result, success = 1)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)