from flask import Flask, request, jsonify
from random import randint

app = Flask(__name__)

# a random comment

db = {
    2: {'name':'orange_juice',
     'price': 20
     },
    3: {'name':'coca_cola',
     'price': 15
     },
    }


@app.route('/')
def index():
    return 'Hello'

@app.route('/drinks/<id>', methods=['POST', 'GET'])
def drinks(id):
    if not id:
        return jsonify(db)
    return db[int(id)]

@app.route('/drinks/', methods=['POST', 'GET'])
def drinks_to_post():
    if request.method == 'POST':
        db[randint(0, 99999)] = {'name': request.json['name'], 'price': request.json['price']}
        return 'Success!'

if __name__ == '__main__':
    app.run()