import pymysql.cursors

import gc

class Database(object):

    DATABASE = None    # static variables

    @staticmethod
    def initialize():
        Database.DATABASE = pymysql.connect(host='localhost',
                                    user='root',
                                    password='root',
                                    db='billing',
                                    unix_socket='/run/mysqld/mysqld.sock',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)


    @staticmethod
    def insert(username,password):

        cursor = Database.DATABASE.cursor()
        sql = "insert into admincredentials(username,password) values(%s,%s)"
        cursor.execute(sql,(username,password))
        cursor.close()
        Database.DATABASE.commit()

        gc.collect()



    @staticmethod
    def find(username):

        cursor = Database.DATABASE.cursor()
        sql = "SELECT * FROM `admincredentials` where `username`=%s"
        cursor.execute(sql, (username))
        cursor.close()

        gc.collect()

        return (cursor.fetchone())

    @staticmethod
    def delete(username):

        cursor = Database.DATABASE.cursor()
        sql = "Delete  FROM `admincredentials` where `username`=%s"
        cursor.execute(sql, (username))
        cursor.close()

        gc.collect()



    @staticmethod
    def update(username, password):

        cursor = Database.DATABASE.cursor()
        sql = "UPDATE `admincredentials` SET `password`=%s where `username`=%s"
        cursor.execute(sql, (password, username))
        cursor.close()

        gc.collect()



if __name__ == '__main__':

    db = Database()
    db.initialize()
