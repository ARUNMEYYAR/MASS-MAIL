import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from valid_email import valid_email

def send_mass_mail(values,attachment):

    mail_subject = values['subject']
    mail_body = values['message']
    user_mail = values['sender_mail']
    receiver_mail_ids = valid_email
    user_password = values['sender_password']
    
    print(receiver_mail_ids)
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = user_mail
    message["Subject"] = mail_subject
    # message["Bcc"] = receiver_email  # Recommended for mass emails
    message['To'] = ", ".join(receiver_mail_ids)
    # Add body to email
    message.attach(MIMEText(mail_body, "plain"))

    filename = attachment  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(user_mail, user_password)
        server.sendmail(user_mail, receiver_mail_ids, text)
