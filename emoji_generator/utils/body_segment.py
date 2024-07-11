import mediapipe as mp

import cv2
import base64
import math
import numpy as np

DESIRED_HEIGHT = 480
DESIRED_WIDTH = 480

BG_COLOR = (255, 255, 255)


def trans_to_bytes(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    _, buffer = cv2.imencode('.png', img)
    img_byte_arr = buffer.tobytes()
    img_base64 = base64.b64encode(img_byte_arr)
    img_base64 = img_base64.decode('ascii')
    return img_base64


def resize_and_show(image):
    h, w = image.shape[:2]
    if h < w:
        img = cv2.resize(image, (DESIRED_WIDTH, math.floor(h/(w/DESIRED_WIDTH))))
    else:
        img = cv2.resize(image, (math.floor(w/(h/DESIRED_HEIGHT)), DESIRED_HEIGHT))
    cv2.imshow("show_img", img)
    cv2.waitKey(0)


def body_segment(img_bytes):
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=True,
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.5,
                        model_complexity=1,
                        smooth_landmarks=True,
                        enable_segmentation=True)

    img_ascii = img_bytes.encode('ascii')
    img_byte_arr = base64.b64decode(img_ascii)
    numpy_image = np.frombuffer(img_byte_arr, np.uint8)
    img_cv_bgr = cv2.imdecode(numpy_image, cv2.IMREAD_COLOR)
    mp_image = cv2.cvtColor(img_cv_bgr, cv2.COLOR_BGR2RGB)

    results = pose.process(mp_image)
    mask = results.segmentation_mask
    mask = mask > 0.6
    mask_3 = np.stack((mask, mask, mask), axis=-1)

    bg_image = np.zeros(mp_image.shape, dtype=np.uint8)
    bg_image[:] = BG_COLOR
    FG_img = np.where(mask_3, mp_image, bg_image)
    BG_img = np.where(~mask_3, mp_image, bg_image)

    # resize_and_show(FG_img)

    img_bytes = trans_to_bytes(FG_img)
    return img_bytes


# img = cv2.imread("../../me.jpg")
# img_bytes = trans_to_bytes(img)
# body_segment(img_bytes)