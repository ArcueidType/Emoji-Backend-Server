from pil_utils import BuildImage
from io import BytesIO
from PIL import Image


def china_flag(image: BuildImage) -> BytesIO:
    img = image.convert("RGBA")
    frame = BuildImage.open("../resources/china_flag.png")
    frame.paste(img.resize(frame.size, keep_ratio=True), below=True)
    return frame.save_jpg()


# img = BuildImage(Image.open('分割丁真.png'))
# img = china_flag(img)
# with open('china_flag.png', 'wb') as file:
#     file.write(img.getvalue())
