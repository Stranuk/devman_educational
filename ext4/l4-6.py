from PIL import Image

original_image = Image.open("red.jpg")

coordinate = (100, 0, original_image.width, original_image.height)
coordinate_middle = (50 , 0, 646, 522)
cropped_left = original_image.crop(coordinate)
cropped_left.save('croped_left_red.jpg')
cropped_middle =original_image.crop(coordinate_middle)
cropped_middle.save('croped_middlr_red.jpg')

image_blend = Image.blend(cropped_left, cropped_middle, 0.5 )
image_blend.save('monro_blanded_red.jpg')