from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello World </h1>'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"


@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f'{number1} + {number2} = {number2+number1}'


@app.route('/handle_url_params')
def handle_params():
    if 'greeting' in request.args.keys() and 'name' in request.args.keys():
        greeting = request.args.get('greeting')
        name = request.args.get('name')
        return f"{greeting}, {name}"
    else:
        return 'Some parameters are missing...'


if __name__ == "__main__":
    app.run(debug=True)


# 2 - 10:34 https://www.youtube.com/watch?v=Jl9XzSPXSe4&list=PL7yh-TELLS1EyAye_UMnlsTGKxg8uatkM&index=2&ab_channel=NeuralNine