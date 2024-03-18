import pandas as pd
import os
import uuid
from flask import Flask, render_template, request, Response, send_from_directory


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

# return a file for download (the same that user uploads is returned to the user in csv form)
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


@app.route('/convert_csv_two', methods=['POST'])
def convert_csv_two():
    file = request.files['uploaded_file']
    df = pd.read_excel(file)

    if not os.path.exists('downloads'):
        os.mkdir('downloads')

    filename = f'{uuid.uuid4()}.csv'
    df.to_csv(os.path.join('downloads',filename))

    return render_template(template_name_or_list='download.html',filename=filename)


@app.route('/download/<filename>')
def download(filename):
    return send_from_directory('downloads', filename, download_name='result.csv')


if __name__ == "__main__":
    app.run(debug=True)


# 26:20 #4