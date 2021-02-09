import random as r


class Battlefield:
    def __init__(self, size):
        self._size = size
        self._current_bg = [[[] for x in range(size)] for x in range(size)]
        self._added_card = []

    def add_card_on_battlefield(self, card):
        self._added_card.append(card)
        return

    @property
    def print_battlefield(self):
        return ''.join(x.card_print for x in self._added_card)


class Card:
    def __init__(self):
        self._card_top_power = r.randint(1, 5)
        self._card_left_power = r.randint(1, 5)
        self._card_right_power = r.randint(1, 5)
        self._card_bottom_power = r.randint(1, 5)

    @property
    def card_print(self):
        return ' {} \n{} {}\n {} \n'.format(self._card_top_power, self._card_left_power, self._card_right_power, self._card_bottom_power)


bg = Battlefield(3)
for y in range(1, 9):
    bg.add_card_on_battlefield(Card())
print(bg.print_battlefield)
