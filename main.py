import random as rnd


class Prisoner:
    def __init__(self, number, choices=50):
        self.number = number
        self.choices = choices

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
    def __init__(self, n_prisoners=100, n_drawers=100):
        self.n_prisoners = n_prisoners
        self.n_drawers = n_drawers

    def __repr__(self):
        return f"Problem({self.n_prisoners}, {self.n_drawers}, math_strategy={self.math_strategy})"

    def __populate(self):
        self.prisoners = [Prisoner(number) for number in range(1, self.n_prisoners + 1)]
        self.drawers = self.__create_drawers()

    def __create_drawers(self):
        drawers_numbers = list(range(1, self.n_drawers + 1))
        cards = list(range(1, self.n_drawers + 1))

        rnd.shuffle(cards)
        args = zip(drawers_numbers, cards)

        return [Drawer(*arg) for arg in args]

    def __exec_math_strategy(self, prisoner):
        success = prisoner.open_drawer(self.drawers[prisoner.number - 1])
        chosen_card = self.drawers[prisoner.number - 1].card

        if success:
            return True

        while prisoner.choices != 0:
            success = prisoner.open_drawer(self.drawers[chosen_card - 1])
            chosen_card = self.drawers[chosen_card - 1].card

            if success:
                return True

        return False

    def __exec_random_strategy(self, prisoner):
        choice_list = list(range(self.n_drawers))
        rnd.shuffle(choice_list)

        for choice in choice_list:
            success = prisoner.open_drawer(self.drawers[choice])

            if success:
                return True

            if prisoner.choices == 0:
                return False

    def start(self, math_strategy=False):
        self.__populate()
        success = []

        if math_strategy:
            for prisoner in self.prisoners:
                success.append(self.__exec_math_strategy(prisoner))

            if all(success):
                return True

            return False

        for prisoner in self.prisoners:
            success.append(self.__exec_random_strategy(prisoner))

        if all(success):
            return True

        return False
