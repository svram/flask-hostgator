from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello world!!! :) Sir'

@app.route('/about')
def about():
	return 'Vikram Bahl is awesome!!'

@app.route('/new')
def new():
	return 'something new'

if __name__ == '__main__':
	app.run(debug=True)
