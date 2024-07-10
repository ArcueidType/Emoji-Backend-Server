# from PIL import Image, ImageDraw, ImageFont
#
# size = 50
# txt = 'hello'
# img = Image.open('1.jpg')
# font = ImageFont.truetype(r'Deng.ttf', size)
# h, w = img.size
#
# l, t, r, b = font.getbbox(txt)
# w1 = r - l
# h1 = b - t
# draw = ImageDraw.Draw(img)
# l, t, r, b = draw.textbbox((0, 0), text=txt, font=font)
# w1 = r - l
# h1 = b - t
#
# draw.text(((w-w1)/2, h/2), txt, fill='white', font=font)
# # draw.text((5, 5), txt, fill='red', font=font)
# img.show()

import requests
import json
from io import BytesIO
import base64
import numpy as np
import cv2
from PIL import Image

with open('1.jpg', 'rb') as f:
    img_data = f.read()


img_base = base64.b64encode(img_data)
img = img_base.decode('ascii')

headers = {'Content-Type': 'application/json'}
data = json.dumps({'img': img, 'text': '我补药玩CS'})

response = requests.post('http://127.0.0.1:5000/graywordmeme', headers=headers, data=data)

img = response.json().get('result')

img = img.encode('ascii')
img = base64.b64decode(img)

img_arr = np.frombuffer(img, dtype=np.uint8)
img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = Image.fromarray(img)
img.show()

