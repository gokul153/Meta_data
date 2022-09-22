import PIL.Image
from PIL import Image
from PIL.ExifTags import TAGS
img1 = PIL.Image.open("padayappa.JPG")
img1
img1.show()
dir(img1)
meta_data = img1.getexif()
meta_data

























