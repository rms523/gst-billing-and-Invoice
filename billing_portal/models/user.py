from flask import session
#from passlib.hash import sha256_crypt
from billing_portal.common.databasesql import Database


class User(object):

    name = ""
    password = ""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def get_by_name(cls,username):
        data = Database.find(username)
        if data is not None:
            return cls(**data)


    @staticmethod
    def login_valid( username, password):
        user = User.get_by_name(username)
        if user is not None:
            try:
                if(user.username == username and user.password == password):
                     return True
            except Exception as e:
                return False

        return False

    @classmethod
    def add_user(cls, username, password ):
        user = cls.get_by_name(username)
        if user is None:
            #password = sha256_crypt.encrypt(str(password))
            Database.insert(username, password)
            session['name'] = username
            return True
        else:
            return False


    @classmethod
    def update_user(cls, username, password):
        user = cls.get_by_name(username)
        if user is not None:
            Database.update(username, password)
            return True
        else:
            return False

    @classmethod
    def delete_user(cls, username, password):
        user = cls.get_by_name(username)
        if user is not None and user.username == username and user.password == password:
            Database.delete(username)
            return True
        else:
            return False

    @staticmethod
    def login(username):
        session['logged_in'] = True
        session['name'] = username

    @staticmethod
    def logout():
        session.clear()






