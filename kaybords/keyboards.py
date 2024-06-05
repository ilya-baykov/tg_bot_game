from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

game_choice_keyboards = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Кости"),
        KeyboardButton(text="БлэкДжек"),
    ]

], resize_keyboard=True, input_field_placeholder="Выберите пункт меню")

dice_game_throws = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Бросить Кости!")
    ]
], input_field_placeholder="Тыкай по кнопке :3")

dice_game_after_game = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Бросить еще раз!"),
        KeyboardButton(text="Назад")
    ]
], input_field_placeholder="Сыграйте еще раз или вернитесь назад")

black_jack_game = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Взять еще карту"),
        KeyboardButton(text="Передать ход боту")
    ]
], input_field_placeholder="Выберите одно из действий")

black_jack_after_game = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Сыграть еще раз!"),
        KeyboardButton(text="Назад"),
    ]
], input_field_placeholder="Сыграйте еще раз или вернитесь назад")
