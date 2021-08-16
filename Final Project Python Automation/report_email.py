#!/usr/bin/env python3

import reports
import os
import datetime
import emails


date_time = today.strftime("%d/%m/%Y")
title = 'Processed Update on '+ date_time
file_list = os.listdir(path)
paragraph = []
for item in file_list:
    opened = open(path + item)

    paragraph.append( 'Name :' + item[0] + '\nWeight :' + item[1] +' lbs' + '\n\n')




if __name__ == "__main__":
    path = os.path.expanduser('~') + "/supplier-data/descriptions/"
    attachment = '/tmp/processed.pdf'
    reports.generate_report(attachment, title, paragraph)
    sender = 'automation@example.com'
    recipient = '{}@example.com'.format(os.environ.get('USER'))
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

    emails.generate_email(sender, recipient, subject, body, attachment)
    emails.send_email()
