from server import api
from flask import jsonify
from flask_restplus import Resource

@api.route('/double/<int:number>')
@api.doc(params={'number': 'Number to be doubled.'}, description='This method doubles the input.')
class DoubleNumber(Resource):
    def get(self, number):
        return jsonify(result=2 * number)