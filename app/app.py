
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

#ตรงส่วนนี้
@app.route('/mul5/<num>', methods=['GET'])
def num_divide_5(num):
    nums = float(num) * 5
    return str(nums)
##################


if __name__ == '__main__':
    app.run(debug=True)




