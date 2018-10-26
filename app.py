from flask import Flask, jsonify, request, render_template

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


@app.route('/')
def home():
    return render_template('index.html')


""" HTTP VERBS
GET - Used to retrieve data only
POST - Used to send data to the server

"""


# GET /store
# @app.route('/')
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# GET /store/<string:mame>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'].lower() == name.lower():
            return jsonify(store)
    return jsonify({'error': True, 'message': 'store not found'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    """
    Iterate over stores list
    If name matches store name return the items in that store
    :param name: store name
    :return: items json
    """
    for store in stores:
        if store['name'].lower() == name.lower():
            return jsonify({'items': store['items']})
    return jsonify({'error': True, 'message': 'Store not found'})


# POST /store data: {name}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)
    return jsonify(new_store)


# POST /store/<string:name>/item {name: price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'].lower() == name.lower():
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'error': True, 'message': 'store not found'})


app.run(port=5000, debug=True)
