from unicodedata import name
import PIL.ExifTags
from PIL import Image
from PIL.ExifTags import TAGS
from gmplot import gmplot
from geopy.geocoders import Nominatim
from gmplot import GoogleMapPlotter

#image =Image.open("IMG_20220921_191451.jpg")
name="padayappa.JPG"
image =Image.open(name)
f=open(name+".txt","w")
info_dict = {
    "Filename": image.filename,
    "Image Size": image.size,
    "Image Height": image.height,
    "Image Width": image.width,
    "Image Format": image.format,
    "Image Mode": image.mode,
    "Image is Animated": getattr(image, "is_animated", False),
    "Frames in Image": getattr(image, "n_frames", 1)
}
exifdata = image.getexif()
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")
    f.write(f"{tag:25}: {data}\n")
print("meta data extracted to"+name+".txt")

exif = {

    PIL.ExifTags.TAGS[k]: v
    for k, v in image._getexif().items()
    if k in PIL.ExifTags.TAGS

        }
#print(exif)
print("From Gpsinformation \n")  
f.write("From Gpsinformation \n")
# priint      
#print(exif['GPSInfo'])
north = exif['GPSInfo'][2]
east = exif['GPSInfo'][4]
#print(north)
#print(east)
lat= float(((((north[0]*60)+north[1])*60)+north[2])/60/60)
long =float(((((east[0]*60)+east[1])*60)+east[2])/60/60)
#print(lat)
#print(long)
gmap = gmplot.GoogleMapPlotter(lat,long,12)
gmap.marker(lat,long,"cornflowerblue")
gmap.draw(name+"location.html")

geoloc= Nominatim(user_agent="GetLoc")
locname = geoloc.geocode(f"{lat}{long}")
locadress = geoloc.reverse(f"{lat},{long}")
#print(locname.address)
print(locadress.address)

f.write(locadress.address)
import webbrowser
webbrowser.open(name+"location.html")