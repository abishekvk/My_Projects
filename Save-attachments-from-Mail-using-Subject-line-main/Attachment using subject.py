# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 13:19:08 2021

@author: abishek.kandiyil
"""


import imaplib
import base64
import os
import email

email_user = 'xyz@outlook.com'
email_pass = input('Password: ')

mail = imaplib.IMAP4_SSL("imap-mail.outlook.com",993)
mail.login(email_user, email_pass)

mail.select()



type, data = mail.search(None, '(OR (SUBJECT "Subject 1") (SUBJECT "Subject 2"))')
mail_ids = data[0]
id_list = mail_ids.split()
print(mail_ids,id_list)

for num in data[0].split():
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]
# converts byte literal to string removing b''
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
# downloading attachments
    for part in email_message.walk():
        # this part comes from the snipped I don't understand yet... 
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue
        fileName = part.get_filename()
        if bool(fileName):
            filePath = os.path.join('C:\MyCodes\python', fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
            subject = 'Given subjects' #str(email_message).split("Subject: ", 1)[1].split("\nTo:", 1)[0]
            print('Downloaded "{file}" from email titled "{subject}" '.format(file=fileName, subject=subject))
             
for response_part in data:
        if isinstance(response_part, tuple):
            msg = email.message_from_string(response_part[1].decode('utf-8'))
            email_subject = msg['subject']
            email_from = msg['from']
            print ('From : ' + email_from + '\n')
            print ('Subject : ' + email_subject + '\n')
            print(msg.get_payload(decode=True))