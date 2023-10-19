
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

#ตรงส่วนนี้
@app.route('/isneg/<num>')
def check_num(num):
    if int(num) >= 0:
        return "False"
    else: 
        return "True"
##################


if __name__ == '__main__':
    app.run(debug=True)




