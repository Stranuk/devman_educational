from PIL import Image

image = Image.open("example.jpg")
print('Ширина - ', image.width)
print('Высота - ', image.height)
print('Цветовая модель - ', image.mode)