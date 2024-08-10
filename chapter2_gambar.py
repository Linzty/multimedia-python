from PIL import Image

# Memuat gambar
image = Image.open('Gambar/sf90.jpg')

# Menyimpan gambar
image.save('output_gambar/result.jpg')

#Cropping image
cropped_image = image.crop((2337, 1769, 6847, 3481))
cropped_image.save('output_gambar/cropped_result.jpg')

#resize image
resized_image = cropped_image.resize((2840 , 1160))
resized_image.save('output_gambar/resized_result.jpg')

#filter image
from PIL import ImageFilter

filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('output_gambar/filtered_result.jpg')