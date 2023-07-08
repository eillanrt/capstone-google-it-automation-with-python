#!/usr/bin/env python
import psutil
import shutil
import socket
import emails
import sys

class HealthCheck:
  def __init__(self):
    self.cpu_usage = self.get_cpu_usage()
    self.disk_usage = self.get_disk_usage()
    self.available_memory = self.get_available_memory()
    self.localhost_ip = self.get_address_ip('localhost')

  def get_cpu_usage(self):
    cpu_percent = psutil.cpu_percent(interval=3)

    return cpu_percent

  def get_disk_usage(self):
    disk_usage = psutil.disk_usage('/')
    disk_percent = disk_usage.percent

    return disk_percent

  def get_available_memory(self):
    memory = psutil.virtual_memory()
    available_memory = memory.available / (1024 ** 2)

    return available_memory

  def get_address_ip(self, address):
    try:
      address_ip = socket.gethostbyname(address)
      return address_ip
    except socket.error as err:
       print(f'Failed to resolve {address}', err)
       return ''

  def diagnose(self):
    error = None

    if self.cpu_usage > 80:
      error = 'Error - CPU usage is over 80%'

    elif self.disk_usage < 20:
      error = 'Error - Available disk space is less than 20%'

    elif self.available_memory < 500:
      error = 'Error - Available memory is less than 500MB'

    elif self.localhost_ip != '127.0.0.1':
      error = 'Error - localhost cannot be resolved to 127.0.0.1'

    return error

  def report_error(self):
    error = self.diagnose()

    if error is None:
      print("Your system seems healthy; No errors to be found :)")
      sys.exit(0)

    error_email = emails.generate_email('automation@example.com', 'user@example.com', error, 'Please check your system and resolve the issue as soon as possible.', None)
    emails.send_email(error_email)

  def __str__(self):
     return 'CPU percent {}\nDisk usage: {}\nAvailable memory: {}\nlocalhost IP: {}'.format(self.cpu_usage,
										    	   self.disk_usage,
											   self.available_memory,
					 						   self.localhost_ip)
def main():
  check = HealthCheck()

  print(check)

  check.report_error()

if __name__ == '__main__':
  main()
