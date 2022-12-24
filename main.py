class Prisoner:
    def __init__(self, number):
        self.number = number
        self.success = False
        self.choices = 50

    def __repr__(self):
        return f"Prisoner({self.number})"
