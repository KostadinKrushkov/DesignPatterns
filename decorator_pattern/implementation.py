import six
import abc


@six.add_metaclass(abc.ABCMeta)
class Notifier:  # The base component
    # @abc.abstractmethod  # if you want to make the class abstract -> to be forced to create concrete notifiers
    def send(self, message):
        print("Notification:" + message)


@six.add_metaclass(abc.ABCMeta)
class BaseNotifierDecorator(Notifier):  # The base decorator
    wrapped_notifier = None

    def __init__(self, wrapped_notifier):
        self.wrapped_notifier = wrapped_notifier


class SMSDecorator(BaseNotifierDecorator):  # A concrete decorator
    def send(self, message):
        self.wrapped_notifier.send(message)
        print("SMS from +123456: " + message)


class FacebookDecorator(BaseNotifierDecorator):
    def send(self, message):
        self.wrapped_notifier.send(message)
        print("Message from Peter Parker: " + message)


class EmailDecorator(BaseNotifierDecorator):
    def send(self, message):
        self.wrapped_notifier.send(message)
        print("You've received an email: " + message)


if __name__ == "__main__":
    notifier = Notifier()
    notifier.send("Hello there!")
    print()

    notifier = SMSDecorator(notifier)
    notifier.send("General Kenobi!")
    print()

    notifier = FacebookDecorator(notifier)
    notifier.send("What's up?")
    print()

    notifier = EmailDecorator(notifier)
    notifier.send("Check this out! www...")
