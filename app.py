from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello World </h1>'

@app.route('/hello')
def hello():
    response = make_response('Hello World')
    response.status_code = 202
    response.headers['content-type']='application/octet-stream'
    return response

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:number1>/<int:number2>')
def add(number1, number2):
    return f'{number1} + {number2} = {number2+number1}'

@app.route('/general', methods=['GET','POST'])
def general():
    if request.method =='GET':
        return 'You made get request\n'
    elif request.method =='POST':
        return 'You made post request\n'
    else:
        return 'You will never see this message'

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
