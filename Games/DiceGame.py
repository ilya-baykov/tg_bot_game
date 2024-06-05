from dataclasses import dataclass, field
from random import randint
from typing import NamedTuple


class Throws(NamedTuple):
    user_throw: int
    bot_throw: int


@dataclass
class DiceGame:
    def __post_init__(self):
        self.__roll_dice()

    def __roll_dice(self):
        self.throws = Throws(user_throw=randint(1, 6), bot_throw=randint(1, 6))

    def determine_winner(self):
        if self.throws.user_throw > self.throws.bot_throw:
            return f"Игрок выиграл. \nВаш счёт:{self.throws.user_throw} \nСчёт Бота:  {self.throws.bot_throw}"
        elif self.throws.bot_throw > self.throws.user_throw:
            return f"Бот выиграл. \nВаш счёт:{self.throws.user_throw}\nСчёт Бота:  {self.throws.bot_throw}"
        else:
            return f"Ничья \nВаш счёт:{self.throws.user_throw} \nСчёт Бота:  {self.throws.bot_throw}"
