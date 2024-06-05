import asyncio
import logging
import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from handlers.handlers import router

from handlers.start_handler import register_start_handlers
from handlers.choice_game_handler import register_choice_game_handlers
from handlers.dice_game_handler import register_dice_game_handlers
from handlers.blackjack_game_handler import register_blackjack_game_handlers

dotenv_path = os.path.join(os.path.dirname(__file__), 'config', '.env')
load_dotenv(dotenv_path)

dp = Dispatcher()
bot = Bot(token=os.getenv('BOT_TOKEN'))


async def main():
    dp.include_router(router)

    # Регистрация обработчиков
    register_start_handlers(dp)
    register_choice_game_handlers(dp)
    register_dice_game_handlers(dp)
    register_blackjack_game_handlers(dp)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
