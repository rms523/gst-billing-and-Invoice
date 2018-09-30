
import pymysql.cursors

import gc

class Database(object):

    DATABASE = None    # static variables

    @staticmethod
    def initialize():
        Database.DATABASE = pymysql.connect(host='localhost',
                                    user='root',
                                    password='supernova',
                                    db='unitedcargo',
                                    unix_socket='/run/mysqld/mysqld.sock',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)


    @staticmethod
    def insert(email,password):

        cursor = Database.DATABASE.cursor()
        sql = "insert into users(email,password) values(%s,%s)"
        cursor.execute(sql,(email,password))
        cursor.close()
        Database.DATABASE.commit()

        gc.collect()



    @staticmethod
    def find(email):

        cursor = Database.DATABASE.cursor()
        sql = "SELECT uid,email,password FROM `users` where `email`=%s"
        cursor.execute(sql, (email))
        cursor.close()

        gc.collect()

        return (cursor.fetchone())
