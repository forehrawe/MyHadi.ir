from flask_mail import Message
from flask import current_app
from __init__ import mail

def send_email(to, subject, html_body):
    msg = Message(
        subject=subject,
        sender=current_app.config['MAIL_USERNAME'],
        recipients=[to]
    )
    msg.html = html_body
    mail.send(msg)
