import smtplib
import getpass

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()

email = getpass.getpass("Email address: ")
password = getpass.getpass("Password: ")  # best practice to generate an app password when testing

smtp_object.login(email, password)


