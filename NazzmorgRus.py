import telebot
from telebot import types
import guessRus as game

new_echo_bot = telebot.TeleBot("850340793:AAEcRbvrX3CRCdJsrLycOZCa7jlzYcNMGBQ")

guess_game = game.GuessGame()


def generate_keyboard():
    markup = types.ReplyKeyboardMarkup()
    markup.one_time_keyboard = True
    markup.row(types.KeyboardButton('1'), types.KeyboardButton('2'), types.KeyboardButton(
        '3'), types.KeyboardButton('4'), types.KeyboardButton('5'))
    markup.row(types.KeyboardButton('6'), types.KeyboardButton('7'), types.KeyboardButton(
        '8'), types.KeyboardButton('9'), types.KeyboardButton('10'))

    return markup


@new_echo_bot.message_handler(commands=['start'])
def handle_start_game(message):
    global guess_game
    new_echo_bot.reply_to(message, guess_game.start_game())
    if guess_game.isPlayable():
        markup = generate_keyboard()
        new_echo_bot.send_message(
            message.chat.id, "Угадай число из представленных ниже:", reply_markup=markup)


@new_echo_bot.message_handler(content_types=['text'])
def handle_guessed_number(message):
    global guess_game
    msg = guess_game.guess_number(int(message.text))
    new_echo_bot.reply_to(message, msg)

    if guess_game.isPlayable():
        markup = generate_keyboard()
        new_echo_bot.send_message(
            message.chat.id, "Угадай число из представленных ниже:", reply_markup=markup)


new_echo_bot.polling(none_stop=True)
