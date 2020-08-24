# !/usr/bin/env/ python3
import requests
from bs4 import BeautifulSoup as bs
import os
import shutil


def download_image():
    # creating a request to the page
    base_url = 'https://www.stocksnap.io'
    url = 'https://stocksnap.io/view-photos/sort/trending/desc'
    response = requests.get(url)
    # to ensure that the connection is successful
    if response.status_code == 200:
        print('connection successul')
    # getting the content of the page
    content = bs(response.content, 'lxml')
    # inding the image classes
    images_a = content.select('.photo-grid-item')  # include the id or class of the div that holds the img
    all_image_url = {}
    for image in images_a:
        try:
            image_url = base_url + image['href']
            image_name = image.img['alt']
            all_image_url[image_name] = image_url
            img_src = image.img['src']
            path = os.path.join('../Pictures/stocksnap/', image_name)
            inner_response = requests.get(img_src, stream=True)
            with open(path, 'wb') as file:
                shutil.copyfileobj(inner_response.raw, file)
        except KeyError:
            pass
    print('all image copied successfully')


if __name__ == '__main__':
    download_image()
