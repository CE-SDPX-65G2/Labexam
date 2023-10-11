
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    return "Hello, " + str(name)


@app.route('/is_prime/<x>', methods=['GET'])
def prime(x):
    num = int(x)
    if num == 0 :
        return True
    else :
        return False
"""
@app.route('/calculate/<num1>/<num2>', methods=['GET'])
def calculate(num1, num2):
    try:
        num1 = eval(num1)
        num2 = int(num2)

        results = {
                'plus' : num1 + num2,
                'minus' : num1 - num2,
                'multiply': num1 * num2,
                'divide' : num1/num2
            }
    except:
        results = { 'error_msg' : 'inputs must be numbers' }

    return jsonify(results)
"""

if __name__ == '__main__':
    app.run()
