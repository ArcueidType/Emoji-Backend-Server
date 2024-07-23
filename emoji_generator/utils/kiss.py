from gif import *


def kiss(image1: BuildImage, image2: BuildImage) -> BytesIO:
    self_head = image1.convert("RGBA").circle().resize((40, 40))
    user_head = image2.convert("RGBA").circle().resize((50, 50))

    user_locs = [
        (58, 90), (62, 95), (42, 100), (50, 100), (56, 100), (18, 120), (28, 110),
        (54, 100), (46, 100), (60, 100), (35, 115), (20, 120), (40, 96)
    ]
    self_locs = [
        (92, 64), (135, 40), (84, 105), (80, 110), (155, 82), (60, 96), (50, 80),
        (98, 55), (35, 65), (38, 100), (70, 80), (84, 65), (75, 65)
    ]

    frames: list[BuildImage] = []
    for i in range(13):
        frame = BuildImage.open('../resources/' + "kiss" + f"/{i}.png")
        frame.paste(user_head, user_locs[i], alpha=True)
        frame.paste(self_head, self_locs[i], alpha=True)
        frames.append(frame)
    return save_gif(frames, 0.05)


# img1 = BuildImage(Image.open('head1.jpg'))
# img2 = BuildImage(Image.open('head2.jpg'))
# gif_data = kiss(img1, img2)
# with open('kiss.gif', 'wb') as file:
#     file.write(gif_data.getvalue())
