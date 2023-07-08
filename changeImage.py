#!/usr/bin/env python
from PIL import Image
import os

images_path = os.path.join('supplier-data', 'images')

def correctify_image(image_path):
  desired_size = (600, 400)

  with Image.open(image_path) as img:
    img.resize(desired_size).convert('RGB').save(image_path, format='jpeg')

def main():
    images_files = [os.path.join(images_path, image_file) for image_file in os.listdir(images_path)]

    for image_file in images_files:
      correctify_image(image_file)
      # print(image_file)


if __name__ == '__main__':
    main()
