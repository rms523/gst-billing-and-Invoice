from flask import session
from passlib.hash import sha256_crypt
from billing_portal.common.databasesql import Database


class User(object):
    def __init__(self, uid, email, password):
        self.email = email
        self.password = password
        self.uid = uid

    @classmethod
    def get_by_email(cls,email):
        data = Database.find(email)
        if data is not None:
            return cls(**data)


    @staticmethod
    def login_valid(email, password):
        user = User.get_by_email(email)
        if user is not None:
            try:
                 if sha256_crypt.verify(password, user.password):
                     return True
            except Exception as e:
                return False

        return False

    @classmethod
    def add_user(cls, email, password ):
        user = cls.get_by_email(email)
        if user is None:
            password = sha256_crypt.encrypt(str(password))
            Database.insert(email, password)
            session['email'] = email
            return True
        else:
            return False


    @staticmethod
    def login(user_email):
        session['logged_in'] = True
        session['email'] = user_email

    @staticmethod
    def logout():
        session.clear()






