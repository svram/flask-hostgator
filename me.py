from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
	resp = Response('Hello world!!! :)')
	resp.headers['Cache-Control'] = 'no-cache'
	return resp

@app.route('/about')
def about():
	return 'About Page'

@app.route('/new')
def new():
	return 'New Page'

if __name__ == '__main__':
	app.run(debug=True)
