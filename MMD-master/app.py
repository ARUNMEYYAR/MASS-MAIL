from flask import *
from werkzeug.utils import secure_filename
from datetime import datetime
import os
from valid_email import *
from send_mail import *

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):

    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

values ={}

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload_csv", methods= ["GET", "POST"])
def verify_csv():

    if request.method == 'POST':

        file = request.files['file']
        if file and allowed_file(file.filename):

            filename = secure_filename(file.filename)
            new_filename = f'{filename.split(".")[0]}_{str(datetime.now())}.csv'
            save_file = os.path.join('csv_files', new_filename)
            file.save(save_file)

            output_file = check_mail(save_file)

        # return 'uploaded'

        # return invalid_email
    # emails = [valid_email, invalid_email]

    return render_template('single.html', invalidmail = invalid_email, validmail = valid_email)
# send mass bulk mail
@app.route("/sendmail", methods=["GET","POST"])
def send_mail():
    # global save_file
    if request.method == 'POST':
        user_mail = request.form['Email']

        sender_password = request.form['pwd']
   
        subject = request.form['subject']
   
        message = request.form['message']

        file = request.files['file']
        
        values['sender_mail'] = user_mail
        values['sender_password'] = sender_password
        values['subject'] = subject
        values['message'] = message
        # if request.method=="POST":
        #     fl=request.files['file']
        filename = secure_filename(file.filename)
        attachment = os.path.join('attachment', filename)
        file.save(attachment)
        # values['attachement'] = save_file
        send_mail = send_mass_mail(values, attachment)

        # if request.method=="POST":
        #     fl=request.files['file']
        #     save_file=fl.save(fl.filename)
        # values['attachment'] = 
        # send_mass_mail(values,)
        
        # print(values)

        print(values)
    return render_template('sendmail.html')

if __name__ == "__main__":

    app.run(host='0.0.0.0', port='5000', debug=True)    