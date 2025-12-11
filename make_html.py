import os
import sys

host_site = "https://yahya-tamur.github.io/go-backgrounds"

image_num = 0
def image_block(image_link,indent=6):
    global image_num
    indent = ' '*indent
    img = f"""{indent}<img src="{image_link}" />\n"""
    button = f"""{indent}<button onclick="click{image_num}()"> copy link </button>\n"""
    script = f"""{indent}<script> click{image_num} = () => {{navigator.clipboard.writeText("{host_site}/{image_link}")}} </script>\n"""
    image_num += 1
    return img+button+script

html = open("schema.html").read()

image_extensions = ['.png']
all_images = [file for file in os.listdir('.') \
        if any(file[-len(ext):] == ext for ext in image_extensions)]

i = 0
while (l := html.find('$#', i)) != -1:
    i = l+1
    r = html.find('#$', l)+2
    block = html[l+2:r-2]
    if block == 'OTHERS':
        continue

    all_images_, block_images = [], []
    for image_link in all_images:
        if block in image_link:
            block_images.append(image_link)
        else:
            all_images_.append(image_link)
    all_images = all_images_


    html = html[:l] + ''.join(image_block(image) for image in block_images) + html[r:]

i = 0
others = "$#OTHERS#$"
while (l := html.find(others, i)) != -1:
    r = l + len(others)

    html = html[:l] + ''.join(image_block(image) for image in all_images) + html[r:]

    i = l + 1

if 'print' in sys.argv:
    print(html)
else:
    open('index.html', 'w').write(html)
    print("Wrote index.html")
