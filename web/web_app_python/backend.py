from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # if we are here we have client data posted
        first_name = request.form['first']
        last_name = request.form['last']
        response_msg = f'Hello {first_name} {last_name}!'
        return render_template('response.html', message=response_msg)
    else:
        # if we are here we send the form to the client
        return render_template('index.html')


# http://127.0.0.1:5000/add?a=100&b=130
@app.route('/add', methods=['GET'])
def add():
    a = int(request.args['a'])
    b = int(request.args['b'])
    sum_ = a + b
    return f'{a} + {b} = {sum_}'


if __name__ == '__main__':
    app.run(debug=True)
