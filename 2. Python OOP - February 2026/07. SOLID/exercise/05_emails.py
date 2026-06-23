from abc import ABC, abstractmethod

class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass

class IContent(ABC):
    @abstractmethod
    def format(self):
        """Return the formatted content as a string."""
        pass


class MyContent(IContent):
    def __init__(self, text):
        self.text = text

    def format(self):
        return "\n".join(["<myML>", self.text, "</myML>"])

class Email(IEmail):
    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender):
        if self.protocol == "IM":
            self.__sender = f"I'm {sender}"
        else:
            self.__sender = sender

    def set_receiver(self, receiver):
        if self.protocol == "IM":
            self.__receiver = f"I'm {receiver}"
        else:
            self.__receiver = receiver

    def set_content(self, content):
        if isinstance(content, IContent):
            self.__content = content.format()
        else:
            self.__content = content

    def __repr__(self):
        template = "Sender: {sender}\nReceiver: {receiver}\nContent:\n{content}"
        return template.format(sender=self.__sender, receiver=self.__receiver, content=self.__content)

email = Email("IM")
email.set_sender("qmal")
email.set_receiver("james")
content = MyContent("Hello, there!")
email.set_content(content)
print(email)