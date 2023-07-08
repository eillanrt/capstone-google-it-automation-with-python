#!/usr/bin/env python
from datetime import date
from run import parse_description_txt, descriptions_path

import os
import reports

def descriptions_to_paragraph():
  descriptions_files = [os.path.join(descriptions_path, file) for file in os.listdir(descriptions_path)]
  descriptions = [parse_description_txt(desc_file) for desc_file in descriptions_files]

  paragraph_description = ''.join(['name: {}\nweight: {} lbs\n\n'.format(desc['name'], desc['weight']) for desc in descriptions])

  return paragraph_description

def main():
  paragraph = descriptions_to_paragraph()
  report_title = 'Processed update {}'.format(date.today())

  reports.generate_report(os.path.join('tmp', 'processed.pdf'), report_title, paragraph)


if __name__ == '__main__':
  main()
