import settings

@settings.BOT.message_handler(commands=['start'])
def start_message(message):
    settings.BOT.send_message(message.chat.id, 'Hello, I am bot that will send you all users that complete authentication.'
                                               'Do you want to see users info ?', settings.KEYBOARD)

@settings.BOT.message_handler(content_types=['text'])
def send_data_from_site(message):
    if message.text == settings.BUTTON_YES:
        file_data = open('users_info.txt', 'r')
        contents = file_data.read()
        settings.BOT.send_message(message.chat.id, f'Here you are:\n {contents}', reply_markup=settings.KEYBOARD)


settings.BOT.polling()