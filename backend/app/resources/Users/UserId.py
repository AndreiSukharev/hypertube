from flask import request
from app.resources.Common.UsersCommon import UsersCommon
from app.resources.Users.Images import Images
from flask_jwt_extended import jwt_required


class UserId(UsersCommon):

    @jwt_required
    def get(self, user_id):
        sql = """
                SELECT  *
                FROM users
                WHERE user_id = %s
            ;"""
        record = (user_id,)
        user = self.base_get_one(sql, record)
        return user

    def delete(self, user_id):
        sql = """DELETE from users WHERE user_id = %s"""
        record = (user_id,)
        res = self.base_write(sql, record)
        return res

    @jwt_required
    def put(self, user_id):
        req_params = dict(request.form)
        params = self.__manage_user_params(req_params, user_id)
        if isinstance(params, str):
            return {'error': params}
        self.__write_userdata_to_db(params, user_id)
        return "ok"

    def __manage_user_params(self, params, user_id):
        checked_params = self.check_user_params(params)
        image_obj = Images()
        result_image = image_obj.handle_images(request.files, user_id)
        if result_image != "ok":
            return result_image
        return checked_params

    @staticmethod
    def check_user_params(params):
        allowed_user_columns = ['email', 'avatar', 'info']
        for key in params.copy():
            if key not in allowed_user_columns:
                del params[key]
        return params

    def __write_userdata_to_db(self, params, user_id):
        for key, value in params.items():
            sql = "UPDATE users SET {} = %s WHERE user_id =%s".format(key)
            if key == "password":
                value = self.to_hash(value)
            record = (value, user_id)
            self.base_write(sql, record)
