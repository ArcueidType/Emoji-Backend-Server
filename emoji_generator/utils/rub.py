from gif import *


def rub(image1: BuildImage, image2: BuildImage) -> BytesIO:
    self_head = image1.convert("RGBA").circle()
    user_head = image2.convert("RGBA").circle()

    user_locs = [
        (39, 91, 75, 75), (49, 101, 75, 75), (67, 98, 75, 75),
        (55, 86, 75, 75), (61, 109, 75, 75), (65, 101, 75, 75)
    ]
    self_locs = [
        (102, 95, 70, 80, 0), (108, 60, 50, 100, 0), (97, 18, 65, 95, 0),
        (65, 5, 75, 75, -20), (95, 57, 100, 55, -70), (109, 107, 65, 75, 0)
    ]

    frames: list[BuildImage] = []
    for i in range(6):
        frame = BuildImage.open('../resources/' + "rub" + f"/{i}.png")
        x, y, w, h = user_locs[i]
        frame.paste(user_head.resize((w, h)), (x, y), alpha=True)
        x, y, w, h, angle = self_locs[i]
        frame.paste(
            self_head.resize((w, h)).rotate(angle, expand=True), (x, y), alpha=True
        )
        frames.append(frame)
    return save_gif(frames, 0.05)


# img1 = BuildImage(Image.open('../黑白丁真.png'))
# img2 = BuildImage(Image.open('../分割丁真.png'))
# gif_data = rub(img1, img2)
# with open('rub.gif', 'wb') as file:
#     file.write(gif_data.getvalue())
