class Prisoner:
    def __init__(self, number):
        self.number = number
        self.success = False
        self.choices = 50

    def __repr__(self):
        return f"Prisoner({self.number})"

    def open_drawer(self, drawer):
        self.choices -= 1
        drawer.opened = True

        return drawer.card


class Drawer:
    def __init__(self, number, card):
        self.number = number
        self.card = card
        self.opened = False

    def __repr__(self):
        return f"Drawer({self.number}, {self.card})"
