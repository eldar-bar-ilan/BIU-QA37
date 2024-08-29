from flask import Flask, request, render_template

app = Flask(__name__)


def index():
    if request.method == 'post':
        # if we are here we have client data posted
        first_name = request.form['first']
        last_name = request.form['last']
        response_msg = f'Hello {first_name} {last_name}!'
        return response_msg
    else:
        # if we are here we send the form to the client
        render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
