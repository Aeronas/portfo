# !Python3                                                  A3R0NA$
from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)
count = 0


@app.route('/')
@app.route('/index.html')
def homeIndex():
    return render_template('index.html')


@app.route('/<string:page_name>')
def load_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    global count
    count += 1
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        body = data["body"]
        database.write(f'''

Message #:{count}
From:{email}
Subject:{subject}
{body}
''')


def write_to_csv(data):
    with open('database.csv', mode='a') as csvdata:
        email = data["email"]
        subject = data["subject"]
        body = data["body"]
        csv_writer = csv.writer(csvdata, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, body])


@app.route('/submit_form', methods=['POST', 'GET'])
# POST returns data to server, GET retrieves data as URL
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/response.html')
    else:
        return 'Something went wrong, try again.'
