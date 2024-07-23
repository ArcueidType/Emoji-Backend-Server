from PIL import ImageOps
from PIL.Image import Image as IMG
from .gif import *


def flash_blind(image: BuildImage, text: str) -> BytesIO:
    img = image.convert("RGB").resize_width(500)
    frames: list[IMG] = [img.image, ImageOps.invert(img.image)]
    img_enlarge = img.resize_canvas((450, img.height * 450 // 500)).resize((500, img.height))
    frames.append(img_enlarge.image)
    frames.append(ImageOps.invert(img.image))

    if text:
        text_h = 65
        try:
            text_frame_black = BuildImage.new("RGBA", (500, text_h), "black")
            text_frame_white = BuildImage.new("RGBA", (500, text_h), "white")
            text_frame_black.draw_text(
                (10, 0, 490, text_h),
                text,
                max_fontsize=50,
                min_fontsize=20,
                fill="white",
            )
            text_frame_white.draw_text(
                (10, 0, 490, text_h),
                text,
                max_fontsize=50,
                min_fontsize=20,
                fill="black",
            )
        except ValueError:
            print("Text too long!")
            return flash_blind(image, "输入文字过长！")

        frames[0].paste(text_frame_black.image, (0, img.height - text_h))
        frames[1].paste(text_frame_white.image, (0, img.height - text_h))
        frames[2].paste(text_frame_black.image, (0, img.height - text_h))
        frames[3].paste(text_frame_white.image, (0, img.height - text_h))

    return save_gif([BuildImage(frame) for frame in frames], 0.04)


# img = BuildImage(Image.open('head1.jpg'))
# gif_data = flash_blind(img, "闪瞎你们的🐕眼")
# with open('flash_blind.gif', 'wb') as file:
#     file.write(gif_data.getvalue())
