class BaseCommand:  # A command needs a receiver
    receiver = None

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        raise NotImplemented()

    def unexecude(self):  # Undo the action from execute
        raise NotImplemented()


class LightsOnCommand(BaseCommand):  # Concrete command
    def execute(self):
        self.receiver.turn_on()

    def unexecute(self):
        self.receiver.turn_off()


class LightsOffCommand(BaseCommand):  # Concrete command
    def execute(self):
        self.receiver.turn_off()

    def unexecute(self):
        self.receiver.turn_on()


class LightsDimUpCommand(BaseCommand):  # Concrete command
    def execute(self):
        self.receiver.dim_up()

    def unexecute(self):
        self.receiver.dim_down()


class LightsDimDownCommand(BaseCommand):  # Concrete command
    def execute(self):
        self.receiver.dim_down()

    def unexecute(self):
        self.receiver.dim_up()


class InvokerLamp:  # Lets say it's a remote control for a lamp
    on_command = None
    off_command = None
    dim_up_command = None
    dim_down_command = None

    def __init__(self, on, off, dim_up, dim_down):
        self.on_command = on
        self.off_command = off
        self.dim_up_command = dim_up
        self.dim_down_command = dim_down

    def click_on(self):
        self.on_command.execute()

    def click_off(self):
        self.off_command.execute()

    def click_dim_up(self):
        self.dim_up_command.execute()

    def click_dim_down(self):
        self.dim_down_command.execute()

    def undo_click_on(self):
        self.on_command.unexecute()

    def undo_click_off(self):
        self.off_command.unexecute()

    def undo_click_dim_up(self):
        self.dim_up_command.unexecute()

    def undo_click_dim_down(self):
        self.dim_down_command.unexecute()

    # def set_command(self, command):  # If ready needed add to change a command functionality
    #     pass


class Receiver:
    light_strength = 0

    def turn_on(self):
        self.light_strength = 1

    def turn_off(self):
        self.light_strength = 0

    def dim_up(self):
        if self.light_strength <= 0.95:
            self.light_strength += 0.05

    def dim_down(self):
        if self.light_strength >= 0.05:
            self.light_strength -= 0.05

    def show_state(self):
        status = "Light's current strength is: {:.2f}/1.".format(self.light_strength) if self.light_strength \
            else "Light is currently off."
        print(status)


if __name__ == "__main__":
    receiver = Receiver()
    invoker = InvokerLamp(LightsOnCommand(receiver), LightsOffCommand(receiver),
                          LightsDimUpCommand(receiver), LightsDimDownCommand(receiver))

    receiver.show_state()
    invoker.click_on()
    receiver.show_state()

    invoker.click_dim_down()
    invoker.click_dim_down()
    receiver.show_state()
    invoker.undo_click_dim_down()
    receiver.show_state()

    invoker.click_off()
    receiver.show_state()
