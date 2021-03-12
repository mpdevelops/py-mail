import imaplib
import getpass
import email

# connect to gmail server
M = imaplib.IMAP4_SSL('imap.gmail.com')

# get email and password from user
email_address = getpass.getpass("Email address: ")
password = getpass.getpass("Password: ")  # best practice to generate an app password when testing

M.login(email_address, password)

# view list of email folders
M.list()

# access inbox
M.select('inbox')

# search emails by subject
typ, data = M.search(None, 'Subject "SUBJECT HERE"')
email_id = data[0]
result, email_data = M.fetch(email_id, '(RFC822')

# decode and print email content
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')
email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)



