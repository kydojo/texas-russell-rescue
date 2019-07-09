from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>I'm home</h1>"

@app.route('/about')
def about():
    return "<h1>About Page</h1>"

# For running the script directly (python app.py)
if __name__=='__main__':
	app.run(debug=True)