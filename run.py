from flask import Flask, request, jsonify
from random import randint

app = Flask(__name__)

db = {
    2: {'name':'orange_juice',
     'price': 20
     },
    3: {'name':'coca_cola',
     'price': 15
     },
    }


@app.route('/drinks/<id>', methods=['GET'])
def drinks(id):
    if not id:
        return jsonify(db)
    return db[int(id)]

@app.route('/drinks/', methods=['POST', 'GET'])
def drinks_to_post():
    '''
    ---------------------------------------------
    POST - METHOD FOR API WILL BE ADD A NEW DRINK
    GET - METHOD TO GET ALL DRINKS
    ---------------------------------------------
    OTHER METODS ARE NOT ALLOWED!
    '''
    if request.method == 'POST':
        db[randint(0, 99999)] = {'name': request.json['name'], 'price': request.json['price']}
        return 'Success!'
    return db

if __name__ == '__main__':
    app.run()