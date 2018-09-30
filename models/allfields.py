from user import Database
import gc

class Allfields():

    @staticmethod
    def fetchallfields():
        cursor = Database.DATABASE.cursor()
        sql = "SELECT * FROM `entry_fields`"
        cursor.execute(sql)
        return (cursor.fetchall())
        Database.DATABASE.close()
        gc.collect()

    @staticmethod
    def saveallfields(li):
        cursor = Database.DATABASE.cursor()
        sql = "insert into entry_fields(creation, grno , pkgs , awt, cwt , invoiceno , sender, receiver, origin , destination, mode , freight) values( %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        cursor.execute(sql,(li[0],li[1],li[2],li[3],li[4],li[5],li[6],li[7],li[8],li[9],li[10],li[11]))
        Database.DATABASE.commit()
        Database.DATABASE.close()
        gc.collect()