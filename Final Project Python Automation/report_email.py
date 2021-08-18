#!/usr/bin/env python3

import reports
import os
import datetime
import emails


date_time = datetime.datetime.today().strftime("%d/%m/%Y")
path = os.path.expanduser('~') + "/supplier-data/descriptions/"
attachment = '/tmp/processed.pdf'
title = 'Processed Update on '+ date_time
file_list = os.listdir(path)

parList = []
for item in file_list:
        with open(path + item, 'r') as opened:
            linesList = opened.readlines()

            parList.append( 'Name : ' + linesList[0].strip() + '<br />' + 'Weight :' + linesList[1].strip() + '<br />' + '<br />')
paragraph = ''.join(parList)



if __name__ == "__main__":



    reports.generate_report(attachment, title, paragraph)
    sender = 'automation@example.com'
    recipient = '{}@example.com'.format(os.environ.get('USER'))
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

    message = emails.generate_email(sender, recipient, subject, body, attachment)
    emails.send_email(message)
