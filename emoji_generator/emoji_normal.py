from pil_utils import BuildImage, Text2Image
from PIL import Image
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
        dy = 30
        dx = 15
        img = BuildImage.new(
            "RGBA", (words.width + dx + shadow_width, words.height + dy + shadow_width)
        )
        img.paste(shadow, (dx - shadow_width, dy - shadow_width), alpha=True)
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

    result = BuildImage.open(os.path.join(RESOURCES_PATH, "bubble.png"))
    exclamation = BuildImage.open(os.path.join(RESOURCES_PATH, "exclamation.png"))

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
