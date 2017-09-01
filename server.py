from flask import *

app = Flask(__name__)

@app.route('/')
def index():
	return 'lul'

app.run()