from flask import Flask, jsonify

app = Flask(__name__)

stores = [
    {
        'name': 'Jenkins',
        'items': [
            {
                'name': 'Converse',
                'price': '$22'
            },
            {
                'name': 'Vans',
                'price': '$15'
            }
        ]
    },
    {
        'name': 'Gal-Paradise',
        'items': [
            {
                'name': 'A thing girls wear',
                'price': '$10'
            },
            {
                'name': 'Another thing girls wear',
                'price': '$10'
            }
        ]
    }
]


# @app.route('/')
# def home():
#     return 'Welcome Home'


""" HTTP VERBS
GET - Used to retrieve data only
POST - Used to send data to the server

"""


# GET /store
@app.route('/')
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# GET /store/<string:mame>
@app.route('/store/<string:name>')
def get_store(name):
    pass


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store():
    pass


# POST /store data: {name}
@app.route('/store', methods=['POST'])
def create_store():
    pass


# POST /store/<string:name>/item {name: price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    pass


app.run(port=5000, debug=True)
