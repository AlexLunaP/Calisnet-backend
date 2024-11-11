from notification.application.service.notification_service import NotificationService


class SendEmailCommand:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def execute(self, to_email: str, subject: str, body: str):
        self.notification_service.send_email(to_email, subject, body)
