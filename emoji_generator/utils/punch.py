from .gif import *


def punch(image: BuildImage) -> BytesIO:
    img = image.convert("RGBA").square().resize((260, 260))
    frames: list[BuildImage] = []
    locs = [
        (-50, 20), (-40, 10), (-30, 0), (-20, -10), (-10, -10), (0, 0),
        (10, 10), (20, 20), (10, 10), (0, 0), (-10, -10), (10, 0), (-30, 10)
    ]
    for i in range(13):
        fist = BuildImage.open(gif_template_root_path + "punch" + f"/{i}.png")
        frame = BuildImage.new("RGBA", fist.size, (255, 255, 255, 0))
        x, y = locs[i]
        frame.paste(img, (x, y - 15), alpha=True).paste(fist, alpha=True)
        frames.append(frame)
    return save_gif(frames, 0.03)


# img = BuildImage(Image.open('head2.jpg'))
# gif_data = punch(img)
# with open('punch.gif', 'wb') as file:
#     file.write(gif_data.getvalue())
