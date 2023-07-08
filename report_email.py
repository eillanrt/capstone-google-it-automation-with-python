#!/usr/bin/env python
from datetime import date
from run import parse_description_txt, descriptions_path

import os
import reports
import emails

def descriptions_to_paragraph():
  descriptions_files = [os.path.join(descriptions_path, file) for file in os.listdir(descriptions_path)]
  descriptions = [parse_description_txt(desc_file) for desc_file in descriptions_files]

  paragraph_description = ''.join(['name: {}\nweight: {} lbs\n\n'.format(desc['name'], desc['weight']) for desc in descriptions])

  return paragraph_description

def main():
  paragraph = descriptions_to_paragraph()
  report_title = 'Processed update {}'.format(date.today())

  report_path = os.path.join('tmp', 'processed.pdf')

  reports.generate_report(report_path, report_title, paragraph)

  message = emails.generate_email('email1@example.com', 'email2@example.com', 'Upload Completed - Online Fruit Store', paragraph, report_path)
  emails.send_email(message)


if __name__ == '__main__':
  main()
