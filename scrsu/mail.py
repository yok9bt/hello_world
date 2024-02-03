import smtplib
from email.message import EmailMessage
def send_mail(to_email, subject, message, server='ssl0.ovh.net',
              from_email='mail'):
    # import smtplib
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ', '.join(to_email)
    msg.set_content(message)
    print(msg)
    server = smtplib.SMTP(server)
    #server.set_debuglevel(1)
    server.login(from_email, 'pass')  # user & password
    server.send_message(msg)
    server.quit()
    print('successfully sent the mail.')

send_mail(to_email=['email'],
          subject='aaa', message='bbb')
