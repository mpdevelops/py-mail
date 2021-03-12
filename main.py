import smtplib
import getpass

# access gmail login server
smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()

# get email and password from user
email = getpass.getpass("Email address: ")
password = getpass.getpass("Password: ")  # best practice to generate an app password when testing
smtp_object.login(email, password)

# send emails
from_address = email
to_address = email
subject = input("Subject: ")
message = input("Email body: ")
msg = "Subject: " + subject + '\n' + message
smtp_object.sendmail(from_address, to_address, msg)

# close connection
smtp_object.quit()



