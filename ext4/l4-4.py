from PIL import Image

image = Image.open("monro.jpg")
red_color_channel, green_color_channel, blue_color_channel = image.split()
red_color_channel.save('red.jpg')
green_color_channel.save('green.jpg')
blue_color_channel.save('blue.jpg')