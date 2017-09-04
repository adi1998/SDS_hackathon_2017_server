from flask import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib

import pandas as pd
import re

app = Flask(__name__)

def preprocess_data(data):
	data = re.sub('\d+',' ',data)
	data = re.sub('[^a-zA-Z0-9 \n]', ' ',data)
	return ' '.join(data.lower().split())

@app.route('/')
def home():
	return "API for SMS classifier"

@app.route('/api/',methods = ['POST'])
@app.route('/api',methods = ['POST'])
def api():
	
	try:
		data = request.form.get('data')
	except:
		return jsonify(spam = 0, success = 0)	
		
	if not data:
		return jsonify(spam = 0, success = 0)

	data = preprocess_data(data)
	df = pd.DataFrame.from_dict({"Message":[data]})["Message"]
	
	model = joblib.load("model.dat")
	vect = joblib.load("vect.dat")

	result = int(model.predict(vect.transform(df).toarray()))
	
	return jsonify(spam = result, success = 1)

if __name__ == '__main__':
    app.run(use_reloader=True)