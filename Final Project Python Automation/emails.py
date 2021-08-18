#!/usr/bin/env python3
from email.message import EmailMessage
import mimetypes
import os
import smtplib

def generate_email(sender, recipient, subject, body, attachment):
    # create email
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    mime_type, _ = mimetypes.guess_type(attachment)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(attachment, 'rb') as attachment_opened:
        message.add_attachment(attachment_opened.read(), maintype = mime_type, subtype = mime_subtype, filename = os.path.basename(attachment))

def generate_email_error(sender, recipient, subject, body):
    # create email
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)    


def send_email():
        """Sends the message to the configured SMTP server."""
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
