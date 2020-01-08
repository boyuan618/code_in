from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
#first page
@app.route('/index')
def index():
    return render_template('index.html')
#second page
@app.route('/about')
def about():
	return render_template('about.html')

'''
if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)
'''
