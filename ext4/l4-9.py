from PIL import Image

image = Image.open("avatar.jpg")
print(image.size) 
image.thumbnail((80, 80))  
print(image.size)
image.save("avatar_thumbnail.jpg")