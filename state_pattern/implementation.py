class GateContext:  # Context
    def __init__(self):
        self.state = ClosedGateState(self)

    def change_state(self, state):
        self.state = state

    def enter(self):
        self.state.enter()

    def pay_ok(self):
        self.state.pay_ok()
        pass

    def pay_failed(self):
        self.state.pay_failed()


class GateState:  # State
    def enter(self):
        pass

    def pay_ok(self):
        pass

    def pay_failed(self):
        pass


class OpenGateState(GateState):  # Concrete State
    def __init__(self, gate_context):
        self.gate = gate_context

    def enter(self):
        print("Allowed one user to pass.")
        self.gate.change_state(ClosedGateState(self.gate))

    def pay_ok(self):
        print("Error. Gate is already open. You may enter.")
        # Refund cash logic

    def pay_failed(self):
        print("Error. Gate is already open. Just enter.")


class ClosedGateState(GateState):  # Concrete State
    def __init__(self, gate_context):
        self.gate = gate_context

    def enter(self):
        print("Error. You need to pay to enter.")

    def pay_ok(self):
        print("You may enter.")
        self.gate.change_state(OpenGateState(self.gate))

    def pay_failed(self):
        print("Error. Insufficient funds, please try again with another card.")


if __name__ == "__main__":
    gate = GateContext()
    print("Default closed\n")
    gate.enter()
    gate.pay_failed()
    gate.pay_ok()

    print("\nOpen\n")
    gate.pay_ok()
    gate.pay_failed()
    gate.enter()
