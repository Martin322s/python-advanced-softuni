from abc import ABC, abstractmethod

class NotificationSender(ABC):
    """
    ISP: minimal interface — all senders can 'send'.
    No construction logic, no sender-type branching here.
    """

    def __init__(self, is_under_maintenance: bool = False):
        self.is_under_maintenance = is_under_maintenance

    @abstractmethod
    def send(self, message: str) -> str:
        """
        Returns feedback (success or maintenance message) instead of raising,
        so any sender remains safely substitutable (LSP).
        """
        pass

class EmailSender(NotificationSender):
    def send(self, message: str) -> str:
        if self.is_under_maintenance:
            return "Email service is currently unavailable (under maintenance)."
        print(f"Sending email with message: {message}")
        return "Email sent successfully."

class SMSSender(NotificationSender):
    def send(self, message: str) -> str:
        if self.is_under_maintenance:
            return "SMS service is currently unavailable (under maintenance)."
        print(f"Sending SMS with message: {message}")
        return "SMS sent successfully."

class PushSender(NotificationSender):
    def send(self, message: str) -> str:
        if self.is_under_maintenance:
            return "Push service is currently unavailable (under maintenance)."
        print(f"Sending Push notification with message: {message}")
        return "Push notification sent successfully."

class NotificationService:
    """
    OCP/SRP: depends on the abstraction (NotificationSender),
    not on concrete types or string-based selection.
    """

    def __init__(self, sender: NotificationSender):
        self.sender = sender

    def notify(self, message: str) -> str:
        return self.sender.send(message)

email_sender = EmailSender()
sms_sender = SMSSender()
push_sender = PushSender()

push_sender.is_under_maintenance = True
"""
The status change represents manual toggling done by an admin or a developer when they know a system component is under maintenance.
In more complex systems, this would be automated or pulled from an external source.
"""

email_service = NotificationService(email_sender)
sms_service = NotificationService(sms_sender)
push_service = NotificationService(push_sender)

print(email_service.notify("Hello via email!"))
print(sms_service.notify("Hello via SMS!"))
print(push_service.notify("Hello via Push!"))