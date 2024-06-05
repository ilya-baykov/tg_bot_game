from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from kaybords import keyboards
from utils.statesforms import BlackJackGameState
from Games.BlackJack import CardDeck52, Player, BotBlackJack
from .start_handler import start_message

router = Router()


@router.message(BlackJackGameState.player_turn)
async def black_jack_game(message: Message, state: FSMContext):
    data = await state.get_data()
    deck: CardDeck52 = data.get('deck')
    player: Player = data.get('player')
    if message.text == "Взять еще карту":
        player.take_turn(deck)
        if player.score > 21:
            await state.set_state(BlackJackGameState.after_game)
            await message.answer(f"Вы проиграли\n{player.hand_cards} = {player.score}очков")
            await message.answer(text="Что вы хотите сделать дальше?", reply_markup=keyboards.black_jack_after_game)
        else:
            await message.answer(text=f"У вас в руке {player.hand_cards} = {player.score}очков")

    elif message.text == "Передать ход боту":
        await state.set_state(BlackJackGameState.bot_turn)
        bot_player = BotBlackJack()
        while bot_player.score <= player.score and bot_player.score < 21:
            bot_player.take_turn(deck)
        if bot_player.score > 21:
            await message.answer(
                text=f"Вы выиграли с {player.score} очками. У бота перебор {bot_player.hand_cards} {bot_player.score} очков",
                reply_markup=keyboards.black_jack_after_game
            )
        else:
            result_text = (f"Бот Выиграл с картами {bot_player.hand_cards} - {bot_player.score} очков"
                           if bot_player.score > player.score else
                           f"Вы выиграли с картами {player.hand_cards} - {player.score} очков")
            await message.answer(text=result_text, reply_markup=keyboards.black_jack_after_game)
        await state.set_state(BlackJackGameState.after_game)
    else:
        await message.answer(text="Я не понял что ты нажал  :(", reply_markup=keyboards.black_jack_game)


@router.message(BlackJackGameState.after_game)
async def black_jack_after_game(message: Message, state: FSMContext):
    if message.text == "Сыграть еще раз!":
        deck = CardDeck52()
        player = Player(deck)
        await state.update_data(deck=deck, player=player)
        await state.set_state(BlackJackGameState.player_turn)
        await message.answer(text=f"Игра БлэкДжек - запущена.\n{player.hand_cards} = {player.score}очков",
                             reply_markup=keyboards.black_jack_game)
    else:
        await state.clear()
        await start_message(message, state=state)


def register_blackjack_game_handlers(dp):
    dp.include_router(router)
