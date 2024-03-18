from flask import Flask, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    my_val = 'Patagonia'
    my_calc = 10 + 20
    my_list = [10, 20, 25,30,40,50]
    return render_template('index.html', myValue = my_val, myCalculation = my_calc, myList = my_list)

@app.route('/other')
def other():
    some_text = 'Patagonia'
    return render_template('other.html', some_text = some_text)

# if you call this endpoint it will redirect to others 
@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('other'))

@app.template_filter('reverse_string')
def reverse_string(s):
    return s[::-1]

@app.template_filter('repeat')
def reverse_string(s, times):
    return s*times

@app.template_filter('alternate_case')
def reverse_string(s):
    return ''.join([c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(s)])

if __name__ == "__main__":
    app.run(debug=True)
