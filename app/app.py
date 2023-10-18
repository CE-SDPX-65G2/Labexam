
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route('/mul5/<num>')
    # BEGIN: num_divide_5
def num_divide_5(num):
    nums = float(num) * 5
    return str(nums)
    # END: num_divide_5



if __name__ == '__main__':
    app.run(debug=True)




