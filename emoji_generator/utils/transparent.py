from PIL import Image
import numpy as np


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
