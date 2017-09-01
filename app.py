from flask import *
from datetime import datetime
app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def homepage():
	try:
		data = request.args.get('data')
	except:
		return jsonify(success = 0)
	#data = preprocess_data(data)
	result = 0 # get from trained model
	return jsonify(spam = result, success = 1)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

