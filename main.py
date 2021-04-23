from flask import Flask, render_template, request, redirect, url_for

import check_phone
import send_message

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        user = request.form['username']
        phone = str(request.form['phone'])

        # check for phone correctness
        phone_check = check_phone.Check_phone(phone)
        if phone_check:
            context = {'user_name' : user, 'phone_number' : phone}
            # send message to the VK
            send_message.Send_message(context)
            print(context)
        return render_template('index.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)