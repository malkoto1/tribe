from flask import Flask, request, make_response
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)
app.config['RESTFUL_JSON'] = {'ensure_ascii': False}


def get_json_as_dict(file):
    with open(file, "r") as fp:
        return json.loads(fp.read())


def write_dict_to_file(file, dictionary):
    with open(file, 'w') as fp:
        fp.write(json.dumps(dictionary))


class Items(Resource):
    def get(self, field=None, search_str=None):
        if field is None:
            return get_json_as_dict("../../resources/items.json")
        return 'Return product based on match of {} field and {} search string'.format(field, search_str)

    def put(self):
        body = request.data.decode('utf-8')
        kor = get_json_as_dict("../../resources/items.json")
        kor[body['id']] = body

        return 200

    def post(self):
        body = request.data.decode('utf-8')
        kor = get_json_as_dict("../../resources/items.json")
        kor[body['id']] = body

        return 200


class Orders(Resource):
    def get(self):
            return get_json_as_dict("../../resources/orders.json")

    def get(self, criteria1=None, criteria2=None):
        return 'all orders between {} and {}'.format(criteria1, criteria2)

    def post(self):
        body = request.data.decode('utf-8')
        print(body)
        return 200


class Stats(Resource):
    def get(self):
        return 'All stats'

    def get(self, which=None):
        if which == 'insufficient':
            return 'All items with not enough quantity'
        elif which == 'recommendation':
            return 'All recommendations'


api.add_resource(Items, '/items', '/items/<field>/<search_str>')
api.add_resource(Orders,
                 '/orders',
                 '/orders/between/<criteria1>/<criteria2>')

api.add_resource(Stats, '/stats', '/stats/<which>')

if __name__ == '__main__':
    app.run(debug=True)
