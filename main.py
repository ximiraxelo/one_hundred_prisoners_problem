import random as rnd


class Drawer:
    def __init__(self, card: int) -> None:
        """Constructs the drawer object

        Args:
            card (int): the number of the card inside the drawer
        """
        self.card = card

    def __repr__(self) -> str:
        return f"Drawer({self.card})"


class Prisoner:
    def __init__(self, number: int, choices: int = 50) -> None:
        """Constructs the prisoner object

        Args:
            number (int): the number of the prisoner
            choices (int, optional): the number of drawers the
            prisoner can open. Defaults to 50.
        """
        self.number = number
        self.choices = choices

    def __repr__(self) -> str:
        return f"Prisoner({self.number})"

    def open_drawer(self, drawer: Drawer) -> bool:
        """Opens a drawer and compares the drawer card with the
        prisoner number

        Args:
            drawer (Drawer): the drawer object to be opened

        Returns:
            bool: the result of the comparison, true for an equality,
            false otherwise.
        """
        if self.number != drawer.card:
            self.choices -= 1
            return False

        return True


class Problem:
    def __init__(self, n_prisoners: int = 100, n_drawers: int = 100) -> None:
        """Constructs the problem object with

        Args:
            n_prisoners (int, optional): the number of prisoners on the
            problem instance. Defaults to 100.
            n_drawers (int, optional): the number of drawers on the
            problem instance. Defaults to 100.
        """
        self.n_prisoners = n_prisoners
        self.n_drawers = n_drawers

    def __repr__(self) -> str:
        return f"Problem({self.n_prisoners}, {self.n_drawers})"

    def __populate(self) -> None:
        self.prisoners = [Prisoner(number) for number in range(1, self.n_prisoners + 1)]
        self.drawers = self.__create_drawers()

    def __create_drawers(self) -> list[Drawer]:
        cards = list(range(1, self.n_drawers + 1))
        rnd.shuffle(cards)

        return [Drawer(card) for card in cards]

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
        """Simulates the problem with a randomly generated set of
        prisoners and drawers

        Args:
            math_strategy (bool, optional): enables the mathematical strategy
            in the simulation of the problem instance. Defaults to False.

        Returns:
            bool: the result of the problem simulation,
            true for prisoners success, false otherwise.
        """
        self.__populate()
        success = []

        if math_strategy:
            for prisoner in self.prisoners:
                prisoner_success = self.__exec_math_strategy(prisoner)

                if not prisoner_success:
                    return False

                success.append(prisoner_success)

            return True

        for prisoner in self.prisoners:
            prisoner_success = self.__exec_random_strategy(prisoner)

            if not prisoner_success:
                return False

            success.append(prisoner_success)

        return True
