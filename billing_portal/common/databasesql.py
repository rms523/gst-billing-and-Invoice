import pymysql.cursors

import gc

class Database(object):

    DATABASE = None    # static variables

    @staticmethod
    def initialize():
        Database.DATABASE = pymysql.connect(host='localhost',
                                    user='root',
                                    password='supernova',
                                    db='billing',
                                    unix_socket='/run/mysqld/mysqld.sock',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)


    @staticmethod
    def insert(username,password):

        cursor = Database.DATABASE.cursor()
        sql = "insert into admincredentials(name,password) values(%s,%s)"
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
    def insertData(data):
        cursor = Database.DATABASE.cursor()
        sql = "insert into invoice_data(date, product, rate, quantity, gstrate, stax, subtotal, total) values(%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
        cursor.close()
        Database.DATABASE.commit()

        gc.collect()


if __name__ == '__main__':
    db = Database()
    db.initialize()
