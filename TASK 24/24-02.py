from PIL import Image


def transparency(n, f):
    image = Image.open(n)
    image1 = Image.open(f)
    w, h = image.size
    for x in range(w):
        for y in range(h):
            pix_coord = (x, y)
            r, g, b = image.getpixel(pix_coord)
            r1, g1, b1 = image1.getpixel(pix_coord)
            new_col = (int(0.5 * r + 0.5 * r1), int(0.5 * g + 0.5 * g1),
                       int(0.5 * b + 0.5 * b1))
            image.putpixel(pix_coord, new_col)
    image.save('res50_transparency.jpg')


transparency("fish.jpg", "space.jpg")
