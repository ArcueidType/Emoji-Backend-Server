import cv2
import os
import math
import onnxruntime as ort
import numpy as np
from PIL import Image

DESIRED_HEIGHT = 1024
DESIRED_WIDTH = 1024
ORIGINAL_HEIGHT = 0
ORIGINAL_WIDTH = 0

cwd = os.getcwd() + "\\emoji_generator\\utils\\AnimeGANv3\\"

model_path = {"宫崎骏": cwd + 'AnimeGANv3_Hayao_36.onnx',
         "新海诚": cwd + 'AnimeGANv3_Shinkai_37.onnx',
         "日本风肖像": cwd + 'AnimeGANv3_JP_face.onnx',
         "素描风肖像": cwd + 'AnimeGANv3_PortraitSketch.onnx'}


def resize(image):
    global ORIGINAL_HEIGHT, ORIGINAL_WIDTH
    h, w = image.shape[:2]
    ORIGINAL_HEIGHT = h
    ORIGINAL_WIDTH = w
    if h * w < DESIRED_HEIGHT * DESIRED_WIDTH:
        return image
    elif h < w:
        img = cv2.resize(image, (DESIRED_WIDTH, math.floor(h/(w/DESIRED_WIDTH))))
    else:
        img = cv2.resize(image, (math.floor(w/(h/DESIRED_HEIGHT)), DESIRED_HEIGHT))
    return img


def process_image(img, model_name):
    h, w = img.shape[:2]
    def to_8s(x):
        if 'tiny' in os.path.basename(model_name) :
            return 256 if x < 256 else x - x % 16
        else:
            return 256 if x < 256 else x - x % 8
    img = cv2.resize(img, (to_8s(w), to_8s(h)))
    img = img.astype(np.float32)/ 127.5 - 1.0
    return img


def load_test_data(image, model_name):
    img = process_image(image, model_name)
    img = np.expand_dims(img, axis=0)
    return img, image.shape


def anime_gen(image, type):
    image = resize(image)
    model = model_path[type]
    session = ort.InferenceSession(model, providers=['CPUExecutionProvider',])
    x = session.get_inputs()[0].name

    sample_image, shape = load_test_data(image, model)
    anime_gen_img = session.run(None, {x: sample_image})
    anime_gen_img = (np.squeeze(anime_gen_img[0]) + 1.) / 2 * 255
    anime_gen_img = np.clip(anime_gen_img, 0, 255).astype(np.uint8)
    result = cv2.resize(anime_gen_img, (ORIGINAL_WIDTH, ORIGINAL_HEIGHT))
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    
    result = Image.fromarray(result)
    # result.show()

    return result


# img = cv2.imread(cwd + "test.jpg")
# anime_gen(img, "新海诚")