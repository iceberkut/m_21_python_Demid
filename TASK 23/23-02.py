from PIL import Image

im = Image.open("Рианна.jpg")
pixels = im.load()
x, y = im.size
rs = []
gs = []
bs = []
for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        rs.append(r)
        gs.append(g)
        bs.append(b)
print(sum(rs) // len(rs), sum(gs) // len(gs), sum(bs) // len(bs))

