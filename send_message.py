import vk

def Send_message(message):
    app_id, login, password = '7835465', 'login@vk.com', 'password'
    session = vk.AuthSession(app_id, login, password, scope='messages')
    vk_api = vk.API(session, v='5.62')

    vk_api.messages.send(user_id="304601652", message=message)