from pil_utils import BuildImage
from io import BytesIO
from PIL import Image


def trance(img: BuildImage) -> BytesIO:
    width, height = img.size
    height1 = int(1.1 * height)
    frame = BuildImage.new("RGB", (width, height1), "white")
    frame.paste(img, (0, int(height * 0.1)))
    img.image.putalpha(3)
    for i in range(int(height * 0.1), int(height * 0.05), -1):
        frame.paste(img, (0, i), alpha=True)
    for i in range(int(height * 0.1), int(height * 0.1 * 2)):
        frame.paste(img, (0, i), alpha=True)
    frame = frame.crop((0, int(0.1 * height), width, height1))
    return frame.save_jpg()


# img = BuildImage(Image.open('img.jpg'))
# gif_data = trance(img)
# with open('trance.jpg', 'wb') as file:
#     file.write(gif_data.getvalue())
