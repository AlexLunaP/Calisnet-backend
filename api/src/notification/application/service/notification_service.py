from flask_mail import Message
from main import mail


class NotificationService:
    def __init__(self):
        pass

    def send_email(self, to_email: str, subject: str, body: str):
        msg = Message(subject, recipients=[to_email], body=body)
        mail.send(msg)
