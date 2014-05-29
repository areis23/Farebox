from flask import Flask, render_template, request
 
app = Flask(__name__)      
 
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/chart', methods=['POST'])
def chart():
	county = request.form['county']
	line = request.form['line']
	return render_template('chart.html', county = county, line = line)

if __name__ == '__main__':
  	app.run(debug=True)