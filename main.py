import random as rnd


class Prisoner:
    def __init__(self, number):
        self.number = number
        self.choices = 50

    def __repr__(self):
        return f"Prisoner({self.number})"

    def open_drawer(self, drawer):
        if self.number != drawer.card:
            self.choices -= 1
            return False

        return True


class Drawer:
    def __init__(self, number, card):
        self.number = number
        self.card = card

    def __repr__(self):
        return f"Drawer({self.number}, {self.card})"


class Problem:
    def __init__(self, n_prisoners=100, n_drawers=100, strategy=False):
        self.n_prisoners = n_prisoners
        self.n_drawers = n_drawers
        self.strategy = strategy

    def __repr__(self):
        return (
            f"Problem({self.n_prisoners}, {self.n_drawers}, strategy={self.strategy})"
        )

    def __create_drawers(self):
        drawers_numbers = list(range(1, self.n_drawers + 1))
        cards = list(range(1, self.n_drawers + 1))

        rnd.shuffle(cards)
        args = zip(drawers_numbers, cards)

        return [Drawer(*arg) for arg in args]

