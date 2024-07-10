from PIL import Image, ImageDraw, ImageFont

size = 50
txt = 'hello'
img = Image.open('1.jpg')
font = ImageFont.truetype(r'Deng.ttf', size)
h, w = img.size

l, t, r, b = font.getbbox(txt)
w1 = r - l
h1 = b - t
draw = ImageDraw.Draw(img)
l, t, r, b = draw.textbbox((0, 0), text=txt, font=font)
w1 = r - l
h1 = b - t

draw.text(((w-w1)/2, h/2), txt, fill='white', font=font)
# draw.text((5, 5), txt, fill='red', font=font)
img.show()
