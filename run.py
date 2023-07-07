#!/usr/bin/env python
import os
import re
import requests

descriptions_path = os.path.join('supplier-data', 'descriptions')

def parse_description_txt(description_path):
  fields = ('name', 'weight', 'description')

  with open(description_path, 'r') as f:
    lines = [line.strip() for line in f.readlines()]
    description = {key: value for key, value in zip(fields, lines)}

  weight_int = re.search(r'^(\d+)', description['weight'])[1]
  description['weight'] = int(weight_int)

  return description

def main():
  descriptions_files = os.listdir(descriptions_path)

  for description in descriptions_files:
    description_path = os.path.join(descriptions_path, description)
    parsed_description = parse_description_txt(description_path)

    res = requests.post('http://localhost:3000/fruits', data=parsed_description)
    print(res.ok)

if __name__ == '__main__':
  main()
