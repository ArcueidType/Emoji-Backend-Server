from flask_restful import Resource
from flask import request
from .utils.body_segment import body_segment


class AddOp(Resource):
    def post(self):
        data = request.get_json()
        num1 = data['num1']
        num2 = data['num2']
        result = num1 + num2
        return {'code': 200, 'msg': 'ok', 'result': result}


class BodySegment(Resource):
    def post(self):
        data = request.get_json()
        img_bytes = data['img']
        result = body_segment(img_bytes)
        return {'code': 200, 'msg': 'ok', 'result': result}

