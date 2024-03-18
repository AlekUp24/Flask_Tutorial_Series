import pandas as pd
from flask import Flask, render_template, request, Response


app = Flask(__name__, template_folder='templates')

@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == 'Hubert' and password == '12345':
            return 'Success'
        else:
            return 'Failure'

@app.route('/file_upload', methods=['POST'])
def file_upload():
    file = request.files['uploaded_file']
    
    if file.content_type == 'text/plain':
        return file.read().decode()
    else:
        return 'File type not recognized.'

@app.route('/convert_csv', methods=['POST'])
def convert_csv():
    file = request.files['uploaded_file']

    df = pd.read_excel(file)
    response = Response(
        df.to_csv(),
        mimetype='text/csv',
        headers = {
            'Content-Disposition': 'attachment; filename=result.csv'
            }
        )

    return response


if __name__ == "__main__":
    app.run(debug=True)


# 20:45 #4