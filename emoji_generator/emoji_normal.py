from pil_utils import BuildImage, Text2Image
from pil_utils.gradient import ColorStop, LinearGradient
from PIL import Image, ImageFilter
from PIL.Image import Resampling, Transform
import os
import math


RESOURCES_PATH = os.path.join(os.getcwd(), 'emoji_generator', 'resources')


def append_text(image: Image, text: str) -> Image:
    image = BuildImage(image)
    if image.width < 100:
        image.resize_width(100)
    if image.height < 100:
        image.resize_height(100)
    width, height = image.width, image.height
    result = BuildImage.new('RGBA', (width, height + round(height / 5)), 'black')
    result.paste(image, alpha=True)
    result.draw_text(
        (10, height + 2, width - 10, height + round(height / 5) - 2),
        text,
        fill='white',
        fontname='GlowSansSC-Normal-Heavy.otf',
        max_fontsize=60
    )
    return result.image


def always(image: Image) -> Image:
    image = BuildImage(image)
    img_large = image.convert('RGBA').resize_width(500)
    img_small = image.convert('RGBA').resize_width(100)

    height_large = img_large.height
    height_small = max(img_small.height, 80)

    result = BuildImage.new('RGBA', (500, height_large + height_small + 10), 'white')
    result.paste(img_large, alpha=True)
    result.paste(
        img_small, (290, height_large + 5 + (height_small - img_small.height) // 2), alpha=True
    )
    result.draw_text(
        (20, height_large + 5, 280, height_large + height_small + 5),
        '要我一直',
        halign='right',
        fontname='./Deng.ttf',
        max_fontsize=60
    )
    result.draw_text(
        (400, height_large + 5, 480, height_large + height_small + 5),
        '吗',
        halign='left',
        fontname='./Deng.ttf',
        max_fontsize=60
    )
    return result.image


def fight_sunuo(image: Image) -> Image:
    image = BuildImage(image)
    image = image.convert('L').resize((565, 1630), keep_ratio=True)

    result = BuildImage.open(os.path.join(RESOURCES_PATH, 'sunuo.png'))
    result.paste(image, (0, 245), below=True)

    return result.image


def ace_attorney(text: str) -> Image:
    def shadow_text_img(text: str, fontsize: int) -> BuildImage:
        font_name = "PangMenZhengDao-Cu.ttf"
        words = Text2Image.from_text(
            text,
            fontsize,
            fill="#e60012",
            fontname=font_name,
            stroke_width=4,
            stroke_fill="#500000",
        ).to_image()
        shadow_width = 10
        shadow = Text2Image.from_text(
            text,
            fontsize,
            fill="#500000",
            fontname=font_name,
            stroke_width=shadow_width,
            stroke_fill="#500000",
        ).to_image()
        y = 30
        x = 15
        img = BuildImage.new(
            "RGBA", (words.width + x + shadow_width, words.height + y + shadow_width)
        )
        img.paste(shadow, (x - shadow_width, y - shadow_width), alpha=True)
        img.paste(words, (0, 0), alpha=True)
        return img

    text_imgs: list[BuildImage] = []
    for char in text:
        text_imgs.append(shadow_text_img(char, 650))

    total_width = sum(img.width for img in text_imgs)
    if total_width > 4000:
        raise ValueError('Too long text: {}'.format(text))

    def combine(text_imgs: list[BuildImage]) -> BuildImage:
        ratio = 0.4
        text_width = sum(img.width for img in text_imgs) - sum(
            round(img.width * ratio) for img in text_imgs[1:]
        )
        text_height = max(img.height for img in text_imgs)
        text_img = BuildImage.new("RGBA", (text_width, text_height))
        x = 0
        for img in text_imgs:
            text_img.paste(img, (x, round((text_height - img.height) / 2)), alpha=True)
            x += img.width - round(img.width * ratio)
        return text_img

    result = BuildImage.open(os.path.join(RESOURCES_PATH, 'bubble.png'))
    exclamation = BuildImage.open(os.path.join(RESOURCES_PATH, 'exclamation.png'))

    if total_width <= 2000:
        text_img = combine(text_imgs)
        max_width = 900
        if total_width > max_width:
            text_img = text_img.resize(
                (max_width, round(max_width / text_img.width * text_img.height))
            )
        text_img = text_img.rotate(10, expand=True)
        result.paste(
            text_img,
            (
                round((result.width - text_img.width) / 2),
                round((result.height - text_img.height) / 2),
            ),
            alpha=True,
        )
        result.paste(exclamation, (630, 230), alpha=True)

    else:
        index = math.ceil(len(text_imgs) / 2)
        text_img1 = combine(text_imgs[:index])
        text_img2 = combine(text_imgs[index:])
        ratio = 0.6
        text_img1 = text_img1.resize(
            (round(text_img1.width * ratio), round(text_img1.height * ratio))
        )
        text_img2 = text_img2.resize(
            (round(text_img2.width * ratio), round(text_img2.height * ratio))
        )
        text_img1 = text_img1.rotate(10, expand=True)
        text_img2 = text_img2.rotate(10, expand=True)
        result.paste(
            text_img1,
            (round((result.width - text_img1.width) / 2) - 50, 775 - text_img1.height),
            alpha=True,
        )
        result.paste(
            text_img2,
            (round((result.width - text_img2.width) / 2) + 50, 325),
            alpha=True,
        )
        result.paste(exclamation, (680, 320), alpha=True)

    return result.image


def colorful(text1: str, text2: str) -> Image:
    fontsize = 200
    font_name = "NotoSerifSC.otf"
    text = text1
    pos_x = 40
    pos_y = 220
    imgs: list[tuple[Image, tuple[int, int]]] = []

    def transform(img: Image) -> Image:
        skew = 0.45
        dw = round(img.height * skew)
        return img.transform(
            (img.width + dw, img.height),
            Transform.AFFINE,
            (1, skew, -dw, 0, 1, 0),
            Resampling.BILINEAR,
        )

    def shift(text_img: Text2Image) -> tuple[int, int]:
        return (
            pos_x
            - text_img.lines[0].chars[0].stroke_width
            - max(char.stroke_width for char in text_img.lines[0].chars),
            pos_y - text_img.lines[0].ascent,
        )

    def add_color_text(stroke_width: int, fill: str, pos: tuple[int, int]):
        text_img = Text2Image.from_text(
            text, fontsize, fontname=font_name, stroke_width=stroke_width, fill=fill
        )
        x, y = shift(text_img)
        imgs.append((transform(text_img.to_image()), (x + pos[0], y + pos[1])))

    def add_gradient_text(
        stroke_width: int,
        dir: tuple[int, int, int, int],
        color_stops: list[tuple[float, tuple[int, int, int]]],
        pos: tuple[int, int],
    ):
        text_img = Text2Image.from_text(
            text, fontsize, fontname=font_name, stroke_width=stroke_width, fill="white"
        )
        mask = transform(text_img.to_image()).convert("L")
        x, y = shift(text_img)
        gradient = LinearGradient(
            (dir[0] - x, dir[1] - y, dir[2] - x, dir[3] - y),
            [ColorStop(*color_stop) for color_stop in color_stops],
        )
        bg = gradient.create_image(mask.size)
        bg.putalpha(mask)
        imgs.append((bg, (x + pos[0], y + pos[1])))

    add_color_text(22, "black", (8, 8))

    add_gradient_text(
        20,
        (0, 38, 0, 234),
        [
            (0.0, (0, 15, 36)),
            (0.1, (255, 255, 255)),
            (0.18, (55, 58, 59)),
            (0.25, (55, 58, 59)),
            (0.5, (200, 200, 200)),
            (0.75, (55, 58, 59)),
            (0.85, (25, 20, 31)),
            (0.91, (240, 240, 240)),
            (0.95, (166, 175, 194)),
            (1, (50, 50, 50)),
        ],
        (8, 8),
    )

    add_color_text(16, "black", (0, 0))

    add_gradient_text(
        10,
        (0, 40, 0, 200),
        [
            (0, (253, 241, 0)),
            (0.25, (245, 253, 187)),
            (0.4, (255, 255, 255)),
            (0.75, (253, 219, 9)),
            (0.9, (127, 53, 0)),
            (1, (243, 196, 11)),
        ],
        (0, 0),
    )

    add_color_text(6, "black", (4, -6))

    add_color_text(6, "white", (0, -6))

    add_gradient_text(
        4,
        (0, 50, 0, 200),
        [
            (0, (255, 100, 0)),
            (0.5, (123, 0, 0)),
            (0.51, (240, 0, 0)),
            (1, (5, 0, 0)),
        ],
        (0, -6),
    )

    add_gradient_text(
        0,
        (0, 50, 0, 200),
        [
            (0, (230, 0, 0)),
            (0.5, (123, 0, 0)),
            (0.51, (240, 0, 0)),
            (1, (5, 0, 0)),
        ],
        (0, -6),
    )

    text = text2

    pos_x = 300
    pos_y = 480

    add_color_text(22, "black", (10, 4))

    add_gradient_text(
        19,
        (0, 320, 0, 506),
        [
            (0, (0, 15, 36)),
            (0.25, (250, 250, 250)),
            (0.5, (150, 150, 150)),
            (0.75, (55, 58, 59)),
            (0.85, (25, 20, 31)),
            (0.91, (240, 240, 240)),
            (0.95, (166, 175, 194)),
            (1, (50, 50, 50)),
        ],
        (10, 4),
    )

    add_color_text(17, "#10193A", (0, 0))

    add_color_text(8, "#D0D0D0", (0, 0))

    add_gradient_text(
        7,
        (0, 320, 0, 480),
        [
            (0, (16, 25, 58)),
            (0.03, (255, 255, 255)),
            (0.08, (16, 25, 58)),
            (0.2, (16, 25, 58)),
            (1, (16, 25, 58)),
        ],
        (0, 0),
    )

    add_gradient_text(
        0,
        (0, 320, 0, 480),
        [
            (0, (245, 246, 248)),
            (0.15, (255, 255, 255)),
            (0.35, (195, 213, 220)),
            (0.5, (160, 190, 201)),
            (0.51, (160, 190, 201)),
            (0.52, (196, 215, 222)),
            (1.0, (255, 255, 255)),
        ],
        (0, -6),
    )

    img_height = 580
    img_width = max([img.width + pos[0] for img, pos in imgs])
    result = BuildImage.new("RGBA", (img_width, img_height), "white")
    for img, pos in imgs:
        result.paste(img, pos, alpha=True)

    return result.image


def ecnu_lion(text: str) -> Image:
    font_name = 'HYBiRanTianTianQuan.ttf'

    result = BuildImage.open(os.path.join(RESOURCES_PATH, 'ecnu_lion.png'))
    result.draw_text(
        (86, 365, 400, 468),
        text=text,
        fontname=font_name,
        max_fontsize=120,
        fill='white'
    )

    return result.image


def ecnu_blackboard(text: str) -> Image:
    font_name = 'HYBiRanTianTianQuan.ttf'

    result = BuildImage.open(os.path.join(RESOURCES_PATH, 'ecnu_blackboard.png'))

    chars = []
    for i, char in enumerate(text):
        chars.append(char)
        if i != len(text) - 1:
            chars.append('\n')

    text = ''.join(chars)

    result.draw_text(
        (375, 70, 475, 260),
        text=text,
        fontname=font_name,
        max_fontsize=120,
        fill='white'
    )

    return result.image


def can_not(image: Image) -> Image:
    image = BuildImage(image)
    image_large = image.convert('RGBA').resize_width(500)
    image_large = image_large.filter(ImageFilter.GaussianBlur(radius=3))
    height_large = image_large.height
    mask = BuildImage.new('RGBA', image_large.size, (0, 0, 0, 32))
    loading = BuildImage.open(os.path.join(RESOURCES_PATH, 'loading.png'))
    image_large.paste(mask, alpha=True).paste(loading, (200, int(height_large / 2) - 50), alpha=True)

    image_small = image.convert('RGBA').resize_width(100)
    height_small = max(image_small.height, 80)

    result = BuildImage.new('RGBA', (500, height_large + height_small + 10), 'white')
    result.paste(
        image_large,
        alpha=True
    ).paste(
        image_small,
        (100, height_large + 5 + (height_small - image_small.height) // 2),
        alpha=True
    )

    result.draw_text(
        (210, height_large + 5, 480, height_large + height_small + 5),
        '不出来',
        halign='left',
        max_fontsize=60,
        fontname='./Deng.ttf'
    )

    return result.image
