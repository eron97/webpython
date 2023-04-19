from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/addition', methods=['POST'])
def addition():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    result = num1 + num2
    return render_template('result.html', result=result)
