from pil_utils import BuildImage
from PIL import Image
from io import BytesIO
from typing import Protocol


gif_template_root_path = '../resources/'
GIF_MAX_FRAMES = 100
GIF_MAX_SIZE = 10


class Maker(Protocol):
    def __call__(self, img: BuildImage) -> BuildImage: ...


class GifMaker(Protocol):
    def __call__(self, i: int) -> Maker: ...


# def fit_gif_template(target_image: BuildImage, gif_name: str, max_frame_index: int, img_w: int) -> list[BuildImage]:
#     img_target_resized = target_image.convert("RGBA").resize_width(img_w)
#     frames = []
#     for frame_index in range(max_frame_index):
#         frame_img = BuildImage.open(gif_template_root_path + gif_name + f"/images/{frame_index}.png")
#         frame_img = frame_img.resize(img_target_resized.size, keep_ratio=True)
#         bg = BuildImage.new("RGB", img_target_resized.size, "white")
#         combined_img = bg.paste(img_target_resized, alpha=True).paste(frame_img, alpha=True)
#         frames.append(combined_img)
#
#     return frames


def save_gif(frames: list[Image], duration: float) -> BytesIO:
    output = BytesIO()
    frames[0].save(
        output,
        format="GIF",
        save_all=True,
        append_images=frames[1:],
        duration=duration * 1000,
        loop=0,
        disposal=2,
        optimize=False,
    )

    nbytes = output.getbuffer().nbytes
    if nbytes <= GIF_MAX_SIZE * 10**6:
        return output

    n_frames = len(frames)
    if n_frames > GIF_MAX_FRAMES:
        index = range(n_frames)
        ratio = n_frames / GIF_MAX_FRAMES
        index = (int(i * ratio) for i in range(GIF_MAX_FRAMES))
        new_duration = duration * ratio
        new_frames = [frames[i] for i in index]
        return save_gif(new_frames, new_duration)

    new_frames = [
        frame.resize((int(frame.width * 0.9), int(frame.height * 0.9)))
        for frame in frames
    ]
    return save_gif(new_frames, duration)


def generate_gif(
        img: BuildImage,
        maker: GifMaker,
        frame_num: int,
        duration: float
) -> BytesIO:
    image = img.image
    return save_gif([maker(i)(img).image for i in range(frame_num)], duration)
