from flask import Flask, render_template, request

import page

app = Flask(__name__,template_folder="template")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_file():
    # Get the uploaded file and the starting/ending page numbers from the form
    file = request.files['file']
    start_page = int(request.form['start_page'])
    end_page = int(request.form['end_page'])

    # Save the uploaded file to the server
    file.save(file.filename)

    # Call the PDF processing function to process the file
    result = page.process_pdf(file.filename, start_page, end_page)

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
