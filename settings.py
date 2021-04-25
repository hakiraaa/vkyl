import telebot

TOKEN = '1657509071:AAHPQNZzCLBVApVtCNjqNxtfCpfgq_wkUZE'
BOT = telebot.TeleBot(TOKEN)

BUTTON_NO = 'NO'
BUTTON_YES = 'YES'


def create_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
    return keyboard


KEYBOARD = create_keyboard()
KEYBOARD.row(BUTTON_NO, BUTTON_YES)