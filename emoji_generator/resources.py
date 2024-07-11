from flask_restful import Resource
from flask import request
import base64
import numpy as np
import cv2
from PIL import Image, ImageFont, ImageDraw
from io import BytesIO
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



class GrayWordMeme(Resource):
    def post(self):
        try:
            data = request.get_json()
            img = data['img']
            text = data['text']

            img = img.encode('ascii')
            img = base64.b64decode(img)
            img_arr = np.frombuffer(img, dtype=np.uint8)
            img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

            height, width, _ = img.shape
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.copyMakeBorder(img, 0, round(height / 5), 0, 0, cv2.BORDER_CONSTANT, value=[0, 0, 0])
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

            img = Image.fromarray(img)
            size = int((height / 5) * 0.75)
            font = ImageFont.truetype(r'./GlowSansSC-Normal-Heavy.otf', size)

            txt_width, txt_height = font.getsize(text)

            draw = ImageDraw.Draw(img)
            draw.text(((width - txt_width) / 2, height + (height // 5 - txt_height) / 2), text, fill='white', font=font)

            buf = BytesIO()
            img.save(buf, 'PNG')
            ret_img = buf.getvalue()
            ret_img = base64.b64encode(ret_img)
            ret_img = ret_img.decode('ascii')

            return {'code': 200, 'msg': 'ok', 'result': ret_img}
        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}
