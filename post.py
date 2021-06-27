import smtplib
import os


def send_email(items, email="lesterdsouza820@gmail.com"):
    with smtplib.SMTP(os.environ['SMTP'], port=587) as connection:
        connection.starttls()
        connection.login(os.environ['EMAIL'], os.environ['PASS'])
        connection.sendmail(os.environ['EMAIL'], email,
                            f"Subject:MESSAGE\n\n"
                            f"Name: {items['name']}\nEmail: {items['email']}\n"
                            f"Phone: {items['phone-number']}\nMessage: {items['textarea']}".encode("utf-8"))