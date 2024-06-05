from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from kaybords import keyboards
from utils.statesforms import ChoiceGameState

router = Router()


@router.message(CommandStart())
async def start_message(message: Message, state: FSMContext):
    await state.set_state(ChoiceGameState.choice_game)
    await message.answer(text="Выберите игру из списка", reply_markup=keyboards.game_choice_keyboards)


def register_start_handlers(dp):
    dp.include_router(router)
