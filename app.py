from flask import Flask, render_template, request
import database



app = Flask(__name__)      
 
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/chart', methods=['POST'])
def chart():
	line = request.form['line']
	line_query = session.query(func.sum(Output.FARE_COLLECTED)).filter_by(LINE_NUMBER = line)
	for result in line_query:
		line_sum= result[0]

	return render_template('chart.html', line= line, line_sum = line_sum)

if __name__ == '__main__':
  	app.run(debug=True)