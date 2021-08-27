from abc import ABCMeta, abstractmethod


class Subject:
    __metaclass__ = ABCMeta

    @abstractmethod
    def request(self):
        raise NotImplemented()


class HeavyweightClass:
    def calculate_data(self):
        print("Crunching numbers...")
        return "Calculated data"


class RealSubject(Subject):
    heavyweight_object = None

    def __init__(self):
        self.heavyweight_object = HeavyweightClass()

    def request(self):
        return self.heavyweight_object.calculate_data()


class LazySubjectProxy(Subject):
    resource_class = None
    resource_instance = None
    data = None
    reset_calculation = True

    def __init__(self, resource_class):
        self.resource_class = resource_class

    def request(self):
        if not self.resource_instance:
            self.resource_instance = self.resource_class()

        # Additional behavior can be added here. For example verifying if user has access to the resource,
        # cache the results, keep a smartlink (if no clients are holding reference to the object destroy it), etc.
        if not self.data or self.reset_calculation:
            self.reset_calculation = False
            self.data = self.resource_instance.request()
        return self.data

    def enable_reset_calculation(self):
        self.reset_calculation = True


if __name__ == "__main__":
    proxy = LazySubjectProxy(RealSubject)
    print(proxy.request())
    print(proxy.request())
    proxy.enable_reset_calculation()  # Used just for the example, the point of the proxy is to have
    # the same functionality as the subject it proxies. It's supposed to decide when to cache or not on it's own.
    print(proxy.request())

