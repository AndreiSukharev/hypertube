from flask_mail import Mail, Message
from flask import current_app
import os


class Email:

    @staticmethod
    def send_new_password(email, password):
        mail = Mail(current_app)
        html = """  <h3>Don't be so stupid, try to remember your password<h3>
                        <p>New Password: {}</p>
                    """.format(password)
        msg = Message(
            subject="Matcha New Password",
            sender=current_app.config.get("MAIL_USERNAME"),
            recipients=[email],
            html=html
        )
        try:
            mail.send(msg)
            return "We have sent new passport to your email"
        except Exception as error:
            print(error)
            return "error"

    @staticmethod
    def send_email_confirmation(email, login, token):
        mail = Mail(current_app)
        host = os.environ['HOST']
        link = "http://{}:5000/api/signup?token={}&login={}".format(host, token, login)
        html = """  <h3>Hello {}!<h3>
                    <p>Thank you for joining our service.</p>
                    <p>To activate your account click the link below.</p>
                    <a href={}>Activate</a>
                """.format(login, link)
        msg = Message(
            subject = "Hypertube Confirmation",
            sender=current_app.config.get("MAIL_USERNAME"),
            recipients=[email],
            html = html
        )
        try:
            mail.send(msg)
            return "We have sent an email confirmation"
        except Exception as error:
            print(error)
            return "error"
