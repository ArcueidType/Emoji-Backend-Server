from flask_restful import Resource
from flask import request


class AddOp(Resource):
    def post(self):
        data = request.get_json()
        num1 = data['num1']
        num2 = data['num2']
        result = num1 + num2
        return {'code': 200, 'msg': 'ok', 'result': result}
