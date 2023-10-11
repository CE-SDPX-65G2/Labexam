
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "ppp"

@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    return "Hello, " + str(name)


@app.route('/is_prime/<x>', methods=['GET'])
def is_prime(x):
    num = int(x)
    # 0 and 1 are not prime numbers
    if num <= 1:
        return "False"
    # Check if the number is divisible by any integer from 2 to the square root of the number
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "False"

    return "True"

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


if __name__ == '__main__':
    app.run()
