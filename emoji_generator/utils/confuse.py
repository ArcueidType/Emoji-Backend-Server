from gif import *


def confuse(image: Image) -> BytesIO:
    image = BuildImage(image)
    img_w = min(image.width, 500)
    frames = fit_gif_template(image, 'confuse', 100, img_w)
    return save_gif(frames, 0.02)


# img = BuildImage(Image.open('丁真.jpg'))
# gif_data = confuse(img)
# with open('confuse.gif', 'wb') as file:
#     file.write(gif_data.getvalue())
