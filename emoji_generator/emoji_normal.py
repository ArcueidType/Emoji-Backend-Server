from pil_utils import BuildImage
from PIL import Image


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
        max_fontsize=60
    )
    result.draw_text(
        (400, height_large + 5, 480, height_large + height_small + 5),
        '吗',
        halign='left',
        max_fontsize=60
    )
    return result.image

