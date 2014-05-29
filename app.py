from flask import Flask, render_template, request
from database2 import db
from sqlalchemy.sql import func



app = Flask(__name__)      
 
@app.route('/')
def home():
	return render_template('home.html')


@app.route('/chart', methods=['POST'])
def chart():
	line = int(request.form['line'])
	#line_sum = get_line_sum()
	return render_template('chart.html', line= line)



if __name__ == '__main__':
  	app.run(debug=True)