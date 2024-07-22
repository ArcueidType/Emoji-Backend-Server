from gif_maker_version import *


def confuse(image: BuildImage) -> BytesIO:
    img_w = min(image.width, 500)

    def maker(i: int) -> Maker:
        def make(img: BuildImage) -> BuildImage:
            img = img.convert("RGBA").resize_width(img_w)
            frame = BuildImage.open(gif_template_root_path + 'confuse' + f"/images/{i}.png").resize(
                img.size, keep_ratio=True
            )
            bg = BuildImage.new("RGB", img.size, "white")
            bg.paste(img, alpha=True).paste(frame, alpha=True)
            return bg

        return make

    return generate_gif(image, maker, 100, 0.02)


img = BuildImage(Image.open('../../img.jpg'))
gif_data = confuse(img)
# gif_data.seek(0)
image = Image.open(gif_data)
image.save('confuse.gif')
