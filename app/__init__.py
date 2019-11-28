from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from binarytree import Node
from app.bst import BST
import random

app = Flask(__name__)
api = Api(app)


class MainResource(Resource):
    def get(self):
        # strip query params
        nodes = request.args.get('nodes')

        if nodes:
            nodes = nodes.split(',')

            shuffle = request.args.get('shuffle')

            if shuffle and shuffle.lower() == 'true':
                random.shuffle(nodes)

            bst = BST()

            try:
                for n in nodes:
                    bst.binary_insert(int(n))
            except:
                return 'An error occurred, please double check your input!'

            response = make_response(bst.get_output(), 200)
            response.mimetype = 'text/plain'

        else:
            response = 'You must supply a comma delimited list of numbers in a \'nodes\' query param!'
        return response


api.add_resource(MainResource, '/')

if __name__ == '__main__':
    app.run()
