from email.message import EmailMessage
import smtplib
import getpass
import os
import mimetypes

def generate(sender, recipient, subject, body, filepath=None):
  message = EmailMessage()

  message['From'] = sender
  message['To'] = recipient
  message['Subject'] = subject

  message.set_content(body)

  if filepath is not None:
    filename = os.path.basename(filepath)
    filetype = mimetypes.guess_type(filepath)[0]

    maintype, subtype = filetype.split('/', 1)

    with open(filepath, 'rb') as f:
      message.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=filename)

  return message

def send(message):
  mail_server = smtplib.SMTP_SSL('smtp.mail.yahoo.com', 465)
  mail_server.set_debuglevel(1)

  email = input('Enter your yahoo email: ')
  email_pass = getpass.getpass('Password for {}: '.format(email))

  assert email == message['From'], 'Your email address should match the sender field'

  mail_server.login(email, email_pass)

  mail_server.send_message(message)

  mail_server.quit()


