from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class Student(Resource):
    def get(self, name):
        return {'student': name.capitalize()}


class Item(Resource):
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item:
            return {'item': item}, 200
        else:
            return {'error': True, 'message': 'No item named {} found'.format(name)}, 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'error': True, 'message': 'An item with name {} already exists.'.format(name)}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class Items(Resource):
    def get(self):
        if len(items) == 0:
            return {'error': True, 'message': 'No items found'}
        return {'items': items}


api.add_resource(Student, '/student/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

app.run(port=5000, debug=True)
