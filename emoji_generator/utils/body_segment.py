import mediapipe as mp

import cv2
import base64
import math
import numpy as np
from PIL import Image

BG_COLOR = (255, 255, 255)

mp_selfie_segmentation = mp.solutions.selfie_segmentation


def trans_to_bytes(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    _, buffer = cv2.imencode('.png', img)
    img_byte_arr = buffer.tobytes()
    img_base64 = base64.b64encode(img_byte_arr)
    img_base64 = img_base64.decode('ascii')
    return img_base64


def body_segment(img_bytes):
    img_ascii = img_bytes.encode('ascii')
    img_byte_arr = base64.b64decode(img_ascii)
    numpy_image = np.frombuffer(img_byte_arr, np.uint8)
    img_cv_bgr = cv2.imdecode(numpy_image, cv2.IMREAD_COLOR)

    mp_image = cv2.cvtColor(img_cv_bgr, cv2.COLOR_BGR2RGB)

    with mp_selfie_segmentation.SelfieSegmentation(model_selection=0) as selfie_segmentation:
        results = selfie_segmentation.process(mp_image)
        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.3
        bg_image = np.zeros(mp_image.shape, dtype=np.uint8)
        bg_image[:] = BG_COLOR
        FG_img = np.where(condition, mp_image, bg_image)
        # BG_img = np.where(~condition, mp_image, bg_image)

        img_bytes = trans_to_bytes(FG_img)
        return img_bytes
