from PIL import Image

red_color_channel = Image.open('monro_blanded_red.jpg')
green_color_channel = Image.open('croped_middle_green.jpg')
blue_color_channel = Image.open('monro_blanded_blue.jpg')
avatar = Image.merge("RGB", (red_color_channel, green_color_channel, blue_color_channel))
avatar.save("avatar.jpg")