from gif import *


def funny_mirror(image: BuildImage) -> BytesIO:
    img = image.convert("RGBA").square().resize((500, 500))
    frames: list[BuildImage] = [img]
    coeffs = [0.01, 0.03, 0.05, 0.08, 0.12, 0.17, 0.23, 0.3, 0.4, 0.6]
    borders = [25, 52, 67, 83, 97, 108, 118, 128, 138, 148]
    for i in range(10):
        new_size = 500 - borders[i] * 2
        new_img = img.distort((coeffs[i], 0, 0, 0)).resize_canvas((new_size, new_size))
        frames.append(new_img.resize((500, 500)))
    frames.extend(frames[::-1])
    return save_gif(frames, 0.05)


# img = BuildImage(Image.open('黑白丁真.png'))
# gif_data = funny_mirror(img)
# with open('funny_mirror.gif', 'wb') as file:
#     file.write(gif_data.getvalue())
