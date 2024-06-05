from aiogram.fsm.state import State, StatesGroup


# Определение состояний

class ChoiceGameState(StatesGroup):
    choice_game = State()


class DiceGameState(StatesGroup):
    roll_dice = State()
    after_game = State()


class BlackJackGameState(StatesGroup):
    player_turn = State()
    bot_turn = State()
    after_game = State()
