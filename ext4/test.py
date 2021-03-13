from PIL import Image

original_image = Image.open("monro.jpg")
indent_size = 100
coordinates_left_indent = (indent_size, 0, original_image.width, original_image.height)
coordinates_right_indent = (0, 0, original_image.width - 100, original_image.height)
coordinates_two_sides = (indent_size / 2 , 0, original_image.width - 50, original_image.height)

red_color_channel, green_color_channel, blue_color_channel = original_image.split()

blend_red_channel = Image.blend(red_color_channel.crop(coordinates_left_indent), red_color_channel.crop(coordinates_two_sides), 0.5)
blend_blue_channel = Image.blend(blue_color_channel.crop(coordinates_right_indent), blue_color_channel.crop(coordinates_two_sides), 0.5)
resized_green_channel = green_color_channel.crop(coordinates_two_sides)

avatar = Image.merge("RGB", (blend_red_channel, resized_green_channel, blend_blue_channel))
avatar.thumbnail((80,80))
avatar.save("avatar.jpg")