class Bill:
    """
    Object that contains data about a bill, such as total amount
    and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Create a flatmate person who lives in the flat
    and pays a share of the bill.
    """

    def __init__(self, name, day_in_house):
        self.name = name
        self.day_in_house = day_in_house

    def pays(self, bill, flatmate2):
        return bill.amount / (self.day_in_house + flatmate2.day_in_house) * self.day_in_house


