from flask import *
from datetime import datetime
app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def homepage():
	data = request.args.get('data')
	#data = preprocess_data(data)
	result = 0 # get from trained model
    return jsonify(
        spam = result
    )

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

