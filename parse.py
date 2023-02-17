import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw
import requests
from io import BytesIO


root = ET.parse('yml_feed.xml').getroot()

сounter = 0
limit = 57
elements = len(root.find('shop/offers'))
for i in root.find('shop/offers'):
    сounter = сounter + 1
    if(сounter<limit):
        continue

    src = i.find('picture').text

    filename = src.split('/')[-1]
    r = requests.get(src)
    print(filename)

    img = Image.open(BytesIO(r.content))
    if '.jpg' in filename:
        print('это jpg')
        new_img = img

    else:
        img = img.convert("RGBA")

        overlay = Image.new('RGBA', img.size, (225, 225, 225, 0))
        new_img = img = Image.alpha_composite(overlay, img)

    new_img.save('imgs/'+filename)



    print("сохранено", сounter, '/', elements)
    # if сounter > 1:
    #     break