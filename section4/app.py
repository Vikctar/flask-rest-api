from flask import Flask
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

    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item


api.add_resource(Student, '/student/<string:name>')
api.add_resource(Item, '/item/<string:name>')

app.run(port=5000, debug=True)
