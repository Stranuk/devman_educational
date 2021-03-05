from PIL import Image

image = Image.open("cmyk.jpg")
cmyk_image = image.convert("RGB")
print('Ширина - ', cmyk_image.width)
print('Высота - ', cmyk_image.height)
print('Цветовая модель - ', cmyk_image.mode)