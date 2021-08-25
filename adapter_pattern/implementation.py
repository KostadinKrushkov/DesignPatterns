class MetricSystem:  # Target
    def derive_distance(self, minutes, velocity):
        return minutes * velocity / 60


class ImperialSystem:  # Adaptee
    def derive_time(self, distance, velocity):
        return distance / velocity

    def derive_veloctiy(self, distance, time):
        return distance / time


class SystemAdapter(ImperialSystem):  # Adapter
    adaptee = None
    distance = None

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def get_distance(self, time, velocity):
        self.distance = self.adaptee.derive_distance(time, velocity)
        return self.translate_distance_to_imperial()

    def translate_distance_to_imperial(self):
        self.distance = self.distance * 0.62137119
        return self.distance

    def translate_distance_to_metric(self):
        self.distance = self.distance / 0.62137119
        return self.distance


class DistanceCalculator:  # Client
    target = None

    def __init__(self, target):
        self.target = target

    def travel(self, time, velocity):
        distance = self.target.get_distance(time, velocity)
        print('With {} minutes and {} km/h, you traveled {} miles'.format(time, velocity, distance))


if __name__ == "__main__":
    adapter = SystemAdapter(MetricSystem())
    calculator = DistanceCalculator(adapter)
    calculator.travel(120, 100)
