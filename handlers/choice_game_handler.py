from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from Games.BlackJack import CardDeck52, Player
from kaybords import keyboards
from utils.statesforms import ChoiceGameState, DiceGameState, BlackJackGameState
from .start_handler import start_message

router = Router()


@router.message(ChoiceGameState.choice_game)
async def choice_game(message: Message, state: FSMContext):
    if message.text == "Кости":
        await state.set_state(DiceGameState.roll_dice)
        await message.answer(text="Игра кости - запущена", reply_markup=keyboards.dice_game_throws)
    elif message.text == "БлэкДжек":
        await state.set_state(BlackJackGameState.player_turn)
        deck = CardDeck52()
        player = Player(deck)
        await state.update_data(deck=deck, player=player)
        await message.answer(text=f"Игра БлэкДжек - запущена.\n{player.hand_cards} = {player.score}очков",
                             reply_markup=keyboards.black_jack_game)
    else:
        await state.clear()
        await start_message(message, state)


def register_choice_game_handlers(dp):
    dp.include_router(router)
