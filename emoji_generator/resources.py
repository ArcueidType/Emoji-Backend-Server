from flask_restful import Resource
from flask import request
import base64
import numpy as np
import cv2
from io import BytesIO
from .utils import *
from .emoji_normal import *
from pil_utils import BuildImage


class AddOp(Resource):
    def post(self):
        try:
            data = request.get_json()
            num1 = data['num1']
            num2 = data['num2']
            result = num1 + num2
            return {'code': 200, 'msg': 'ok', 'result': result}
        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class BodySegment(Resource):
    def post(self):
        try:
            data = request.get_json()
            img_bytes = data['img']

            result = body_segment(img_bytes)

            return {'code': 200, 'msg': 'ok', 'result': result}
        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


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

            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

            img = Image.fromarray(img)

            img = append_text(img, text)

            buf = BytesIO()
            img.save(buf, 'PNG')
            ret_img = buf.getvalue()
            ret_img = base64.b64encode(ret_img)
            ret_img = ret_img.decode('ascii')

            return {'code': 200, 'msg': 'ok', 'result': ret_img}
        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class Always(Resource):
    def post(self):
        try:
            data = request.get_json()
            img = data['img']

            img = img.encode('ascii')
            img = base64.b64decode(img)

            img_arr = np.frombuffer(img, dtype=np.uint8)
            img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)

            img = always(img)

            buf = BytesIO()
            img.save(buf, 'PNG')
            ret_img = buf.getvalue()
            ret_img = base64.b64encode(ret_img)
            ret_img = ret_img.decode('ascii')

            return {'code': 200, 'msg': 'ok', 'result': ret_img}

        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class FightSunuo(Resource):
    def post(self):
        try:
            data = request.get_json()
            img = data['img']

            img = img.encode('ascii')
            img = base64.b64decode(img)

            img_arr = np.frombuffer(img, dtype=np.uint8)
            img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)

            img = fight_sunuo(img)

            buf = BytesIO()
            img.save(buf, 'PNG')
            ret_img = buf.getvalue()
            ret_img = base64.b64encode(ret_img)
            ret_img = ret_img.decode('ascii')

            return {'code': 200, 'msg': 'ok', 'result': ret_img}

        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class AnimeGen(Resource):
    def post(self):
        try:
            data = request.get_json()
            img = data['img']
            type = data['type']

            img = img.encode('ascii')
            img = base64.b64decode(img)
            img_arr = np.frombuffer(img, dtype=np.uint8)
            img = cv2.imdecode(img_arr, cv2.IMREAD_UNCHANGED)
            img = Image.fromarray(img)
            mask = mask_alpha(img)
            img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

            img = anime_gen(img, type)

            img = restore_alpha(img, mask)
            buf = BytesIO()
            img.save(buf, 'PNG')
            result = buf.getvalue()
            result = base64_RGBA_encode(result)

            return {'code': 200, 'msg': 'ok', 'result': result}
        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class AceAttorney(Resource):
    def post(self):
        try:
            data = request.get_json()
            text = data['text']

            img = ace_attorney(text)

            buf = BytesIO()
            img.save(buf, 'PNG')
            ret_img = buf.getvalue()
            ret_img = base64.b64encode(ret_img)
            ret_img = ret_img.decode('ascii')

            return {'code': 200, 'msg': 'ok', 'result': ret_img}

        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class Colorful(Resource):
    def post(self):
        try:
            data = request.get_json()
            text1 = data['text1']
            text2 = data['text2']

            img = colorful(text1, text2)

            buf = BytesIO()
            img.save(buf, 'PNG')
            ret_img = buf.getvalue()
            ret_img = base64.b64encode(ret_img)
            ret_img = ret_img.decode('ascii')

            return {'code': 200, 'msg': 'ok', 'result': ret_img}

        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class ECNULion(Resource):
    def post(self):
        try:
            data = request.get_json()
            text = data['text']

            img = ecnu_lion(text)

            buf = BytesIO()
            img.save(buf, 'PNG')
            result = buf.getvalue()
            result = base64.b64encode(result)
            result = result.decode('ascii')

            return {'code': 200, 'msg': 'ok', 'result': result}
        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class ECNUBlackboard(Resource):
    def post(self):
        try:
            data = request.get_json()
            text = data['text']

            img = ecnu_blackboard(text)

            buf = BytesIO()
            img.save(buf, 'PNG')
            result = buf.getvalue()
            result = base64.b64encode(result)
            result = result.decode('ascii')

            return {'code': 200, 'msg': 'ok', 'result': result}
        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class CanNot(Resource):
    def post(self):
        try:
            data = request.get_json()
            img = data['img']

            img = img.encode('ascii')
            img = base64.b64decode(img)

            img_arr = np.frombuffer(img, dtype=np.uint8)
            img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)

            img = can_not(img)

            buf = BytesIO()
            img.save(buf, 'PNG')
            ret_img = buf.getvalue()
            ret_img = base64.b64encode(ret_img)
            ret_img = ret_img.decode('ascii')

            return {'code': 200, 'msg': 'ok', 'result': ret_img}

        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class LuXun(Resource):
    def post(self):
        try:
            data = request.get_json()
            text = data['text']

            img = lu_xun(text)

            buf = BytesIO()
            img.save(buf, 'PNG')
            ret_img = buf.getvalue()
            ret_img = base64.b64encode(ret_img)
            ret_img = ret_img.decode('ascii')

            return {'code': 200, 'msg': 'ok', 'result': ret_img}

        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class BlueArchive(Resource):
    def post(self):
        try:
            data = request.get_json()
            text1 = data['text1']
            text2 = data['text2']

            img = blue_archive(text1, text2)

            buf = BytesIO()
            img.save(buf, 'PNG')
            ret_img = buf.getvalue()
            ret_img = base64.b64encode(ret_img)
            ret_img = ret_img.decode('ascii')

            return {'code': 200, 'msg': 'ok', 'result': ret_img}

        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class Confuse(Resource):
    def post(self):
        try:
            data = request.get_json()
            img = data['img']
            img = base64_RGBA_decode(img)

            gif_bytes = confuse(img).getvalue()

            result = base64_RGBA_encode(gif_bytes)
            return {'code': 200, 'msg': 'ok', 'result': result}
        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class FlashBlind(Resource):
    def post(self):
        try:
            data = request.get_json()
            img = data['img']
            text = data['text']
            img = base64_RGBA_decode(img)

            gif_bytes = flash_blind(BuildImage(img), text).getvalue()

            result = base64_RGBA_encode(gif_bytes)
            return {'code': 200, 'msg': 'ok', 'result': result}
        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class Trance(Resource):
    def post(self):
        try:
            data = request.get_json()
            img = data['img']
            img = base64_RGBA_decode(img)

            gif_bytes = trance(BuildImage(img)).getvalue()

            result = base64_RGBA_encode(gif_bytes)
            return {'code': 200, 'msg': 'ok', 'result': result}
        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class Play(Resource):
    def post(self):
        try:
            data = request.get_json()
            img = data['img']
            img = base64_RGBA_decode(img)

            gif_bytes = play(BuildImage(img)).getvalue()

            result = base64_RGBA_encode(gif_bytes)
            return {'code': 200, 'msg': 'ok', 'result': result}
        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class ChaseTrain(Resource):
    def post(self):
        try:
            data = request.get_json()
            img = data['img']
            img = base64_RGBA_decode(img)

            gif_bytes = chase_train(BuildImage(img)).getvalue()

            result = base64_RGBA_encode(gif_bytes)
            return {'code': 200, 'msg': 'ok', 'result': result}
        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class FunnyMirror(Resource):
    def post(self):
        try:
            data = request.get_json()
            img = data['img']
            img = base64_RGBA_decode(img)

            gif_bytes = funny_mirror(BuildImage(img)).getvalue()

            result = base64_RGBA_encode(gif_bytes)
            return {'code': 200, 'msg': 'ok', 'result': result}
        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class GuiChu(Resource):
    def post(self):
        try:
            data = request.get_json()
            img = data['img']
            direction = data['text']
            img = base64_RGBA_decode(img)

            gif_bytes = guichu(BuildImage(img), direction).getvalue()

            result = base64_RGBA_encode(gif_bytes)
            return {'code': 200, 'msg': 'ok', 'result': result}
        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class Punch(Resource):
    def post(self):
        try:
            data = request.get_json()
            img = data['img']
            img = base64_RGBA_decode(img)

            gif_bytes = punch(BuildImage(img)).getvalue()

            result = base64_RGBA_encode(gif_bytes)
            return {'code': 200, 'msg': 'ok', 'result': result}
        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class Kiss(Resource):
    def post(self):
        try:
            data = request.get_json()
            img1 = data['img1']
            img2 = data['img2']
            img1 = base64_RGBA_decode(img1)
            img2 = base64_RGBA_decode(img2)

            gif_bytes = kiss(BuildImage(img1), BuildImage(img2)).getvalue()

            result = base64_RGBA_encode(gif_bytes)
            return {'code': 200, 'msg': 'ok', 'result': result}
        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}


class Rub(Resource):
    def post(self):
        try:
            data = request.get_json()
            img1 = data['img1']
            img2 = data['img2']
            img1 = base64_RGBA_decode(img1)
            img2 = base64_RGBA_decode(img2)

            gif_bytes = rub(BuildImage(img1), BuildImage(img2)).getvalue()

            result = base64_RGBA_encode(gif_bytes)
            return {'code': 200, 'msg': 'ok', 'result': result}
        except Exception as e:
            return {'code': 500, 'msg': f'Process Procedure Error: {e}'}
