import os
from PIL import Image

im_files = os.listdir('Pics')
try:
    im_files.remove('.DS_Store')
except:
    pass

for im_file in im_files:
    file_name = 'Pics' + os.sep + im_file
    im = Image.open(file_name)
    im.thumbnail((800, 600))
    print(im.format, im.size, im.mode)
    im.save(file_name)
    print('Done!')