#!/usr/bin/env python3

import os
import shutil
import psutil
import emails
import socket

# cpu usage float percentage
cpu = psutil.cpu_percent()

# disk as tuple (total, used, free)
path = ("/")
memory = shutil.disk_usage(path)
free = memory.free
twenty_per_cent =  (memory.total/100)*20

# RAM available
THRESHOLD = 500 * 1024 * 1024  # 500MB
ram = psutil.virtual_memory() # has available method

# define hostname
hostname = socket.gethostbyname('localhost')

# email paramaters
sender = "automation@example.com"
recipient = "{}@example.com".format(os.environ.get('USER'))
body = "Please check your system and resolve the issue as soon as possible."

def health_check(cpu, ram, hostname):
    if cpu > 80:
        subject = 'Error - CPU usage is over 80%'
        message = emails.generate_email_error(sender, recipient, subject, body)
        emails.send_email(message)
    if free > twenty_per_cent:
        subject = 'Disk space less than 20'
        message = emails.generate_email_error(sender, recipient, subject, body)
        emails.send_email(message)
    if ram.available < THRESHOLD:
        subject = 'Ram less than 500'
        message = emails.generate_email_error(sender, recipient, subject, body)
        emails.send_email(message)

    if hostname != '127.0.0.1':
        subject = 'local host is not 127.0.0.1'
        message = emails.generate_email_error(sender, recipient, subject, body)
        emails.send_email(message)

health_check(cpu, ram, hostname)
