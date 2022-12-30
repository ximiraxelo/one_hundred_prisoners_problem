import random as rnd


class Drawer:
    def __init__(self, number: int, card: int) -> None:
        """Constructs the drawer object

        Args:
            number (int): the number of the drawer
            card (int): the number of the card inside the drawer
        """        
        self.number = number
        self.card = card

    def __repr__(self) -> str:
        return f"Drawer({self.number}, {self.card})"


class Prisoner:
    def __init__(self, number: int, choices: int = 50) -> None:
        """Constructs the prisoner object

        Args:
            number (int): the number of the prisoner
            choices (int, optional): the number of drawers the prisoner can open. Defaults to 50.
        """        
        self.number = number
        self.choices = choices

    def __repr__(self) -> str:
        return f"Prisoner({self.number})"

    def open_drawer(self, drawer: Drawer) -> bool:
        """Opens a drawer and compares the drawer card with the prisoner number

        Args:
            drawer (Drawer): the drawer object to be opened

        Returns:
            bool: the result of the comparison, true for an equality, false otherwise.
        """        
        if self.number != drawer.card:
            self.choices -= 1
            return False

        return True


class Problem:
    def __init__(self, n_prisoners: int = 100, n_drawers: int = 100) -> None:
        self.n_prisoners = n_prisoners
        self.n_drawers = n_drawers

    def __repr__(self) -> str:
        return f"Problem({self.n_prisoners}, {self.n_drawers})"

    def __populate(self) -> None:
        self.prisoners = [Prisoner(number) for number in range(1, self.n_prisoners + 1)]
        self.drawers = self.__create_drawers()

    def __create_drawers(self) -> list[Drawer]:
        drawers_numbers = list(range(1, self.n_drawers + 1))
        cards = list(range(1, self.n_drawers + 1))

        rnd.shuffle(cards)
        args = zip(drawers_numbers, cards)

        return [Drawer(*arg) for arg in args]

    def __exec_math_strategy(self, prisoner: Prisoner) -> bool:
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

    def __exec_random_strategy(self, prisoner: Prisoner) -> bool:
        choice_list = list(range(self.n_drawers))
        rnd.shuffle(choice_list)

        for choice in choice_list:
            success = prisoner.open_drawer(self.drawers[choice])

            if success:
                return True

            if prisoner.choices == 0:
                break

        return False

    def start(self, math_strategy: bool = False) -> bool:
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
