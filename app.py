from flask import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import  GaussianNB
from pickle import load

import pandas as pd
import numpy as np
import re


app = Flask(__name__)

def preprocess_data(data):
	data = re.sub('\d+',' ',data)
	data = re.sub('[^a-zA-Z0-9 \n]', ' ',data)
	return ' '.join(data.lower().split())

@app.route('/',methods = ['GET', 'POST'])
def homepage():
	data = request.args.get('data')
	if not data:
		return jsonify(success = 0)

	data = preprocess_data(data)
	
	df = pd.DataFrame.from_dict({'Message':[data]})["Message"]
	
	
	vect = load(file('vect.dat'))
	model = load(file('model.dat'))
	print vect.transform(df).toarray()
	result = int(model.predict(vect.transform(df).toarray()))
	print (result)
	
	return jsonify(spam = result, success = 1)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)