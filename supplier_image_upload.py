#!/usr/bin/env python
import os
import requests

images_path = os.path.join('supplier-data', 'images')

def upload(image_path):
  with open(image_path, 'rb') as opened:
    res = requests.post('http://localhost:3000/upload', files={'file': opened})
    print(res.ok)

def main():
  for image in os.listdir(images_path):
    image_path = os.path.join(images_path, image)
    upload(image_path)

if __name__ == '__main__':
  main()
