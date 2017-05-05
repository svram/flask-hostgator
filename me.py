from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	resp = flask.Response('Hello world!!! :) Sir')
	resp.headers['Cache-Control'] = 'no-cache'
	return resp

@app.route('/about')
def about():
	return 'Vikram Bahl is awesome!!'

@app.route('/new')
def new():
	return 'something new'

if __name__ == '__main__':
	app.run(debug=True)
