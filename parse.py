import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw
import requests
from io import BytesIO


root = ET.parse('feed.xml').getroot()

сounter = 0
# limit = 57 Страртуем от 57
elements = len(root.find('shop/offers'))
no_aplfa = []
for i in root.find('shop/offers'):
    сounter = сounter + 1
    # if(сounter<limit):
    #     continue

    src = i.find('picture').text

    filename = src.split('/')[-1]
    r = requests.get(src)
    # print(filename)

    img = Image.open(BytesIO(r.content))
    img.thumbnail(size=(600, 600))

    if '.jpg' in filename:
        print('это jpg')
        new_img = img

    else:
        img = img.convert("RGBA")

        pix = img.load()
        apl = pix[1, 1][3]
        if apl !=0:
            print(src)
            no_aplfa.append(src)

        overlay = Image.new('RGBA', img.size, '#ffffff')

        new_img = Image.alpha_composite(overlay, img)

    save_flag = new_img.save('imgs/'+filename)
    if save_flag == False:
        print('не сохранено', src)
        break

    print("сохранено", сounter, '/', elements, save_flag)
    # if сounter > 1:
    #     break


print(len(no_aplfa))