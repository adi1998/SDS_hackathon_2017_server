from flask import *
from datetime import datetime
app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def homepage():
	data = request.args.get('data')
	if not data:
		return jsonify(success = 0)

	#data = preprocess_data(data)

	# get from trained model
	result = 0 
	
	return jsonify(spam = result, success = 1)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

