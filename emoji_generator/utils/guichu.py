from typing import NamedTuple

from .gif import *
from PIL.Image import Transpose


def guichu(image: BuildImage, direction: str) -> BytesIO:
    img = image.convert("RGBA")
    img_w, img_h = img.size

    if direction not in ['left', 'right', 'top', 'bottom', '上', '下', '左', '右']:
        direction = 'left'
    elif direction == '左':
        direction = 'left'
    elif direction == '右':
        direction = 'right'
    elif direction == '上':
        direction = 'top'
    elif direction == '下':
        direction = 'bottom'

    class Mode(NamedTuple):
        method: Transpose
        size1: tuple[int, int, int, int]
        pos1: tuple[int, int]
        size2: tuple[int, int, int, int]
        pos2: tuple[int, int]

    modes: dict[str, Mode] = {
        "left": Mode(
            Transpose.FLIP_LEFT_RIGHT,
            (0, 0, img_w // 2, img_h),
            (0, 0),
            (img_w // 2, 0, img_w // 2 * 2, img_h),
            (img_w // 2, 0),
        ),
        "right": Mode(
            Transpose.FLIP_LEFT_RIGHT,
            (img_w // 2, 0, img_w // 2 * 2, img_h),
            (img_w // 2, 0),
            (0, 0, img_w // 2, img_h),
            (0, 0),
        ),
        "top": Mode(
            Transpose.FLIP_TOP_BOTTOM,
            (0, 0, img_w, img_h // 2),
            (0, 0),
            (0, img_h // 2, img_w, img_h // 2 * 2),
            (0, img_h // 2),
        ),
        "bottom": Mode(
            Transpose.FLIP_TOP_BOTTOM,
            (0, img_h // 2, img_w, img_h // 2 * 2),
            (0, img_h // 2),
            (0, 0, img_w, img_h // 2),
            (0, 0),
        ),
    }

    mode = modes[direction]
    img_flip = img.transpose(mode.method)
    img_symmetric = BuildImage.new("RGBA", img.size)
    img_symmetric.paste(img.crop(mode.size1), mode.pos1, alpha=True)
    img_symmetric.paste(img_flip.crop(mode.size2), mode.pos2, alpha=True)
    img_symmetric_big = BuildImage.new("RGBA", img.size)
    img_symmetric_big.paste(
        img_symmetric.copy().resize_width(img_w * 2), (-img_w // 2, -img_h // 2)
    )

    frames: list[BuildImage] = []
    frames += (
        ([img] * 3 + [img_flip] * 3) * 3
        + [img, img_flip] * 3
        + ([img_symmetric] * 2 + [img_symmetric_big] * 2) * 2
    )

    return save_gif(frames, 0.2)


# img = BuildImage(Image.open('黑白丁真.png'))
# gif_data = guichu(img, '右')
# with open('guichu.gif', 'wb') as file:
#     file.write(gif_data.getvalue())
