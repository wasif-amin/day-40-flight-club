import os
import smtplib
from dotenv import load_dotenv
load_dotenv()
class NotificationManager:

    def __init__(self):
        self.email = os.environ.get("EMAIL")
        self.email_password = os.environ.get("EMAIL_PASSWORD")
        self.RECIPIENT = os.environ.get("RECIPIENT")
        self.connection = smtplib.SMTP("smtp.gmail.com")


    # def send_email(self, message_body):
    #     with smtplib.SMTP("smtp.gmail.com") as connection:
    #         connection = smtplib.SMTP("smtp.gmail.com")
    #         connection.starttls()
    #         connection.login(user=self.EMAIL, password=self.PASSWORD)
    #         connection.sendmail(
    #         from_addr=self.EMAIL,
    #         to_addrs=self.RECIPIENT,
    #         msg=message_body)

    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(self.email, self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email,
                    to_addrs=email,
                    msg=f"subject:New low price flight!\n\n{email_body}".encode("utf-8")
                )






