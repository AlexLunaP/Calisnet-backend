import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class FlaskMailService:
    def __init__(self, gmail_user, gmail_password):
        self.gmail_user = gmail_user
        self.gmail_password = gmail_password

    def send_email(self, to_email: str, subject: str, body: str):
        msg = MIMEMultipart()
        msg["From"] = self.gmail_user
        msg["To"] = to_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(self.gmail_user, self.gmail_password)
            text = msg.as_string()
            server.sendmail(self.gmail_user, to_email, text)
            server.quit()
        except Exception as e:
            print(f"Failed to send email: {e}")
