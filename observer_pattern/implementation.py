class BaseObservable:
    def register_observer(self, observer):
        pass

    def unregister_observer(self, observer):
        pass

    def notify(self):  # Broadcast changes to the state, it should be used when the state of the observable changes
        pass


class BaseObserver:
    def update(self):  # Called by the observable
        pass


class DogCollar(BaseObservable):  # ConcreteObservable, Different observables may have different states,
    # for example a dog may need to take a walk but a cat may need attention
    observers_list = []
    _need_to_eat = None
    _need_to_drink = None
    _need_to_walk = None
    _need_to_poop = None

    def __init__(self, need_to_eat, need_to_drink, need_to_walk, need_to_poop):
        self._need_to_eat = need_to_eat
        self._need_to_drink = need_to_drink
        self._need_to_walk = need_to_walk
        self._need_to_poop = need_to_poop

    def register_observer(self, observer):
        self.observers_list.append(observer)
        observer.update()  # Sending state to observer immediately after registering is optional

    def unregister_observer(self, observer):
        self.observers_list.remove(observer)

    def notify(self):
        for observer in self.observers_list:
            observer.update()

    def get_state(self):
        return self.need_to_eat, self.need_to_drink, self.need_to_walk, self.need_to_poop

    @property
    def need_to_eat(self):
        return self._need_to_eat

    @need_to_eat.setter
    def need_to_eat(self, value):
        self._need_to_eat = value
        self.notify()

    @property
    def need_to_drink(self):
        return self._need_to_drink

    @need_to_drink.setter
    def need_to_drink(self, value):
        self._need_to_drink = value
        self.notify()

    @property
    def need_to_walk(self):
        return self._need_to_walk

    @need_to_walk.setter
    def need_to_walk(self, value):
        self._need_to_walk = value
        self.notify()

    @property
    def need_to_poop(self):
        return self._need_to_poop

    @need_to_poop.setter
    def need_to_poop(self, value):
        self._need_to_poop = value
        self.notify()


class Phone(BaseObserver):  # ConcreteObserver
    animal_observable = None
    need_to_do = ""

    def __init__(self, animal_observable):
        self.animal_observable = animal_observable

    def update(self):
        self.need_to_do = ""
        eat, drink, walk, poop = self.animal_observable.get_state()
        if eat:
            self.need_to_do += "Needs to be fed.\n"
        if drink:
            self.need_to_do += "Needs water in bowl.\n"
        if walk:
            self.need_to_do += "Needs a walk.\n"
        if poop:
            self.need_to_do += "Needs to go now!\n"

    def show_state(self):
        message = self.need_to_do if self.need_to_do else "Your pet doesn't need anything right now\n"
        print("\nPhone--\nYour pet's state has changed \n" + message + "--\n")


class SmartWatch(BaseObserver):  # ConcreteObserver
    animal_observable = None
    need_to_do = ""

    def __init__(self, animal_observable):
        self.animal_observable = animal_observable

    def update(self):
        self.need_to_do = ""
        eat, drink, walk, poop = self.animal_observable.get_state()
        if eat:
            self.need_to_do += "Needs to be fed.\n"
        if drink:
            self.need_to_do += "Needs water in bowl.\n"
        if walk:
            self.need_to_do += "Needs a walk.\n"
        if poop:
            self.need_to_do += "Needs to go now!\n"

    def show_state(self):
        message = self.need_to_do if self.need_to_do else "Your pet doesn't need anything right now"
        print("Watch --\nNotification from your pet \n" + message + "--\n")


# Simulating the changes in state of the registered observables, the observers will always have up to date information
if __name__ == "__main__":
    animal_sensor = DogCollar(False, True, True, False)
    phone = Phone(animal_sensor)
    watch = SmartWatch(animal_sensor)

    animal_sensor.register_observer(phone)
    animal_sensor.register_observer(watch)

    phone.show_state()
    animal_sensor.need_to_eat = True
    watch.show_state()
    animal_sensor.need_to_eat = False
    animal_sensor.need_to_walk = False
    animal_sensor.need_to_drink = False
    phone.show_state()

    # After unsubscribing the observer will not longer be updated when the state changes
    animal_sensor.unregister_observer(watch)
    animal_sensor.need_to_poop = True
    phone.show_state()
    watch.show_state()
