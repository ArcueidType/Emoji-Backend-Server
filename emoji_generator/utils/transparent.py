from PIL import Image
import numpy as np
import base64
import cv2


def base64_RGBA_decode(img: str) -> Image:
    img = img.encode('ascii')
    img = base64.b64decode(img)
    img_arr = np.frombuffer(img, dtype=np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
    img = Image.fromarray(img)
    return img


def base64_RGBA_encode(gif: bytes) -> str:
    result = base64.b64encode(gif)
    result = result.decode('ascii')
    return result


def mask_alpha(img):
    img_data = np.array(img)
    mask = np.zeros(img_data.shape[:2], dtype=bool)
    if img_data.shape[2] == 4:
        alpha_channel = img_data[:, :, 3]
        mask = alpha_channel == 0
    return mask


def restore_alpha(img, mask):
    img_data = np.array(img)
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
        img_data = np.array(img)
    if img_data.shape[2] == 4:
        img_data[:, :, 3][mask] = 0
    restored_img = Image.fromarray(img_data)
    return restored_img
