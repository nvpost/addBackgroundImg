import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw
import requests
from io import BytesIO


root = ET.parse('yml_feed.xml').getroot()

сounter = 0
for i in root.find('shop/offers'):
    src = i.find('picture').text


    filename = src.split('/')
    # output_url = dir + "/" + filename
    r = requests.get(src)


    img = Image.open(BytesIO(r.content))
    img = img.convert("RGBA")


    overlay = Image.new('RGBA', img.size, (225, 225, 225))
    new_img = img = Image.alpha_composite(overlay, img)

    new_img.save('imgs/'+filename[-1])
    сounter = сounter +1
    if сounter > 1:
        break