from app.resources.Common.UsersCommon import UsersCommon
from flask import request
from app.resources.loginPage.Email import Email


class SignUp(UsersCommon):

    # when user follow the link in email to activate an account
    def get(self):
        token = request.args["token"]
        login = request.args["login"]
        record = (login,)
        if not self.__check_email_token(record, token):
            return "incorrect token"
        self.__change_user_status(record)
        return "Activated"

    def post(self):
        email = request.json['email']
        login = request.json['login']
        password = self.to_hash(request.json['password'])
        token = self.to_hash((email+login))

        record = (email, login, password, token)
        sql = '''INSERT INTO users (email, login, password, token)
                 VALUES (%s, %s, %s, %s);'''
        if self.base_write(sql, record) == "ok":
            res = Email.send_email_confirmation(email, login, token)
            return res
        return "Email or login already exist"

    def __check_email_token(self, record, token):
        sql = '''SELECT token FROM users
                 WHERE login = %s
                ;'''
        token_dict = self.base_get_one(sql, record)
        if not token_dict:
            return 0
        if token_dict['token'] == token:
            return 1
        else:
            return 0

    def __change_user_status(self, record):
        sql = "UPDATE users SET status = '1' WHERE login =%s;"
        self.base_write(sql, record)

    def get_user_id(self, record):
        sql = '''SELECT user_id FROM users
                 WHERE login = %s
                ;'''
        user_id = self.base_get_one(sql, record)
        return user_id['user_id']
