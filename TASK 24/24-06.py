from PIL import Image


def make_preview(size, n_colors):
    im = Image.open('image.jpg')
    im = im.resize(size)
    im = im.quantize(n_colors)
    im.save('24-06.bmp')


make_preview((400, 200), 64)
