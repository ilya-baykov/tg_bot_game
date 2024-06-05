from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from kaybords import keyboards
from utils.statesforms import DiceGameState
from Games.DiceGame import DiceGame
from .start_handler import start_message

router = Router()


@router.message(DiceGameState.roll_dice)
async def dice_game_roll_dice(message: Message, state: FSMContext):
    dice_game = DiceGame()
    winner = dice_game.determine_winner()
    await message.answer(text=winner)
    await state.set_state(DiceGameState.after_game)
    await message.answer(text="Что вы хотите сделать дальше?", reply_markup=keyboards.dice_game_after_game)


@router.message(DiceGameState.after_game)
async def dice_game_after_game(message: Message, state: FSMContext):
    if message.text == "Назад":
        await state.clear()
        await start_message(message, state)
    else:
        await state.set_state(DiceGameState.roll_dice)
        await dice_game_roll_dice(message, state)


def register_dice_game_handlers(dp):
    dp.include_router(router)
