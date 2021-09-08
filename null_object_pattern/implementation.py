import random

DEFAULT_PLAN_ID = "0"


class ICustomer:
    def is_none(self):
        pass

    def get_plan(self):
        pass


class Customer(ICustomer):
    def is_none(self):
        return False

    def get_plan(self):
        return Plan()


class NoneCustomer(ICustomer):
    def is_none(self):
        return True


class Plan:
    def __init__(self):
        self.title = f"Plan_title_{random.randint(1, 10000)}"

    def __repr__(self):
        return f"Plan title: {self.title}"


def get_default_plan():
    default_plan = Plan()
    default_plan.title = f"Plan_title_{DEFAULT_PLAN_ID}"
    return default_plan


def get_customer_plan(customer):
    if customer.is_none():
        return get_default_plan()
    else:
        return customer.get_plan()


if __name__ == "__main__":
    customer = Customer()
    print(get_customer_plan(customer))

    customer = NoneCustomer()
    print(get_customer_plan(customer))
