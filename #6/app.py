from flask import Flask, render_template, session

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')
app.secret_key = 'SOME KEY'


@app.route('/')
def index():
    return render_template('index.html', message = 'INDEX')

@app.route('/set_data')
def set_data():
    session['name'] = 'Mike'
    session['other'] = 'Hello World'

    return render_template('index.html', message = 'Session data set.')

@app.route('/get_data')
def get_data():
    if 'name' in session.keys() and 'other' in session.keys():
        name = session['name']
        other = session['other']
        return render_template('index.html', message = f'Name is {name} and other is {other}')
    else:
        return render_template('index.html', message = 'No session found.')

@app.route('/clear_session')
def clear_session():
    session.clear()
    return render_template('index.html', message = 'Session celared!')

if __name__ == "__main__":
    app.run(debug=True)
