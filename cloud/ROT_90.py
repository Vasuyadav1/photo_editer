import numpy as np
from PIL import Image

img = np.array(Image.open('C:/Users/muskan kumari/anaconda3/envs/class_267/cloud/cute_cat.png'))
print(type(img))

print(img.shape)

Image.fromarray(np.rot90(img)).save('cute_cat_rot90.png')

Image.fromarray(np.rot90(img, 2)).save('cute_cat_rot90_180.png')

Image.fromarray(np.rot90(img, 3)).save('cute_cat_rot90_270.png')

im_flip = ImageOps.flip(img)
im_flip.save('cute_cat_flip.png', quality=95)

im_mirror = ImageOps.mirror(img)
im_mirror.save('cute_cat_mirror.png', quality=95)