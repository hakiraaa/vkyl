from flask import Flask, render_template, request

import check_phone


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        user = request.form['username']
        phone = str(request.form['phone'])

        # check for phone correctness
        phone_check = check_phone.Check_phone(phone)
        if phone_check:
            context = {'Name' : user, 'Phone' : phone}
            # save data in a file
            data_file = open('users_info.txt', 'a')
            data_file.write(f'{context}\n')
            data_file.close()
        return render_template('index.html')
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)