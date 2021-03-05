from PIL import Image

red_color_channel = Image.open('red.jpg')
green_color_channel = Image.open('green.jpg')
blue_color_channel = Image.open('blue.jpg')
new_image = Image.merge("RGB", (red_color_channel, green_color_channel, blue_color_channel))
new_image.save('new_monro.jpg')
