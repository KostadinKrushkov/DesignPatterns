class BaseTransportStrategy:  # Base strategy
    def find_best_route(self, starting_point, ending_point):
        raise NotImplemented()


class WalkStrategy(BaseTransportStrategy):  # Concrete strategy
    def find_best_route(self, starting_point, ending_point):
        return "Strategy for walking(from {}, to {})".format(starting_point, ending_point)


class DriveStrategy(BaseTransportStrategy):  # Concrete strategy
    def find_best_route(self, starting_point, ending_point):
        return "Strategy for driving (from {}, to {})".format(starting_point, ending_point)


class PublicTransportStrategy(BaseTransportStrategy):  # Concrete strategy
    def find_best_route(self, starting_point, ending_point):
        return "Stategy for taking public transport (from {}, to {})".format(starting_point, ending_point)


class Navigator:  # Acts like context -> holds reference to the strategy
    best_path_strategy = WalkStrategy()  # default strategy

    def set_strategy(self, strategy):
        self.best_path_strategy = strategy

    def get_route_to(self, destination):
        starting_point = self.get_starting_point()
        return self.best_path_strategy.find_best_route(starting_point, destination)

    def get_starting_point(self):
        return "Your location"


if __name__ == "__main__":
    navigator = Navigator()
    destination = "Sofia, Mladost 4"
    print(navigator.get_route_to(destination))

    navigator.set_strategy(DriveStrategy())
    print(navigator.get_route_to(destination))

    navigator.set_strategy(PublicTransportStrategy())
    print(navigator.get_route_to(destination))
