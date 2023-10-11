from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message':'Hello, World!'})

@app.route('/is_prime/<int:num>', methods=['GET'])
def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return 'False'
        else:
            return 'True'
    else:
        return 'Flase'

if __name__ == '__main__':
    app.run(debug=True)