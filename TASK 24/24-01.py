from PIL import Image, ImageChops


def twist_image(input_file_name, output_file_name):
    im = Image.open(input_file_name)
    x, _ = im.size
    im = ImageChops.offset(im, x // 2, 0)
    im.save(output_file_name)


twist_image('statement-image.jpg', '24-01.jpg')
