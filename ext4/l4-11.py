from PIL import Image

original_image = Image.open("monro.jpg")

coordinate_left = (100, 0, 696, 522)
coordinate_right = (0, 0, 596, 522)
coordinate_middle = (50 , 0, 646, 522)

red_color_channel, green_color_channel, blue_color_channel = original_image.split()

red_color_channel_blend = Image.blend(red_color_channel.crop(coordinate_left), red_color_channel.crop(coordinate_middle), 0.5)
blue_color_channel_blend = Image.blend(blue_color_channel.crop(coordinate_right), blue_color_channel.crop(coordinate_middle), 0.5)
green_color_channel_crop_middle = green_color_channel.crop(coordinate_middle)

avatar = Image.merge("RGB", (red_color_channel_blend, green_color_channel_crop_middle, blue_color_channel_blend))
avatar.thumbnail((80,80))
avatar.save("avatar.jpg")

#avatar_thumbnail_80_80.save('avatar.jpg')