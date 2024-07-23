from .gif import *


def play(image: BuildImage) -> BytesIO:
    img = image.convert("RGBA").square()

    locs = [
        (180, 60, 100, 100), (184, 75, 100, 100), (183, 98, 100, 100),
        (179, 118, 110, 100), (156, 194, 150, 48), (178, 136, 122, 69),
        (175, 66, 122, 85), (170, 42, 130, 96), (175, 34, 118, 95),
        (179, 35, 110, 93), (180, 54, 102, 93), (183, 58, 97, 92),
        (174, 35, 120, 94), (179, 35, 109, 93), (181, 54, 101, 92),
        (182, 59, 98, 92), (183, 71, 90, 96), (180, 131, 92, 101)
    ]

    raw_frames: list[BuildImage] = [
        BuildImage.open('../resources/' + "play" + f"/{i}.png") for i in range(38)
    ]
    img_frames: list[BuildImage] = []
    for i in range(len(locs)):
        frame = raw_frames[i]
        x, y, w, h = locs[i]
        frame.paste(img.resize((w, h)), (x, y), below=True)
        img_frames.append(frame)
    frames = (
        img_frames[0:12]
        + img_frames[0:12]
        + img_frames[0:8]
        + img_frames[12:18]
        + raw_frames[18:38]
    )
    return save_gif(frames, 0.06)


# img = BuildImage(Image.open('head1.jpg'))
# gif_data = play(img)
# with open('play.gif', 'wb') as file:
#     file.write(gif_data.getvalue())
