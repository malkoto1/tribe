from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Items(Resource):
    def get(self):
        return 'all items'

    def get(self, field=None, search_str=None):
        return 'Return product based on match of {} field and {} search string'.format(field, search_str)


class Orders(Resource):
    def get(self):
        return 'all orders'

    def get(self, criteria1=None, criteria2=None):
        return 'all orders between {} and {}'.format(criteria1, criteria2)

    def post(self):
        body = request.data.decode('utf-8')
        print(body)
        return 200


api.add_resource(Items, '/items', '/items/<field>/<search_str>')
api.add_resource(Orders,
                 '/orders',
                 '/orders/between/<criteria1>/<criteria2>')

if __name__ == '__main__':
    app.run(debug=True)
