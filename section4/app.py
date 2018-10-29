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
        for item in items:
            if item['name'].lower() == name.lower():
                return item
        return {'error': 'No item named {} found'.format(name)}, 404

    def post(self, name):
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class Items(Resource):
    def get(self):
        return {'items': items}


api.add_resource(Student, '/student/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

app.run(port=5000, debug=True)
