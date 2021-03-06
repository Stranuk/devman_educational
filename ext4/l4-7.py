from PIL import Image

original_image = Image.open("blue.jpg")
print('Ширина - ', original_image.width)
print('Высота - ', original_image.height)
coordinate = (0, 0, 596, 522)
coordinate_middle = (50 , 0, 646, 522)
cropped_left = original_image.crop(coordinate)
cropped_left.save('croped_left_blue.jpg')
cropped_middle =original_image.crop(coordinate_middle)
cropped_middle.save('croped_middle_blue.jpg')

image_blend = Image.blend(cropped_left, cropped_middle, 0.5 )
image_blend.save('monro_blanded_blue.jpg')