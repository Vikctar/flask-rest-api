from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from section4.security import authenticate, identity

app = Flask(__name__)  # type: Flask
app.secret_key = 'k1ll3r'
# noinspection PyTypeChecker
api = Api(app)

jwt = JWT(app, authenticate, identity)
items = []


class Student(Resource):
    def get(self, name):
        return {'student': name.capitalize()}


class Item(Resource):
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item:
            return {'item': item}, 200
        else:
            return {'error': True, 'message': 'No item named {} found'.format(name)}, 404

    @jwt_required()
    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'error': True, 'message': 'An item with name {} already exists.'.format(name)}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class Items(Resource):
    @jwt_required()
    def get(self):
        if len(items) == 0:
            return {'error': True, 'message': 'No items found'}
        return {'items': items}


# noinspection PyTypeChecker
api.add_resource(Student, '/student/<string:name>')
# noinspection PyTypeChecker
api.add_resource(Item, '/item/<string:name>')
# noinspection PyTypeChecker
api.add_resource(Items, '/items')

app.run(port=5000, debug=True)
