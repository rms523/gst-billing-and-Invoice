from billing_portal.models.user import Database
import gc

class Allfields():

    @staticmethod
    def fetchallfields():
        cursor = Database.DATABASE.cursor()
        sql = "SELECT * FROM `invoice_data`"
        cursor.execute(sql)
        cursor.close()
        gc.collect()
        return (cursor.fetchall())


    @staticmethod
    def saveallfields(data):
        cursor = Database.DATABASE.cursor()
        sql = "insert into invoice_data(date, product, rate, quantity, gstrate, stax, subtotal, total) values(%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7]))
        cursor.close()
        Database.DATABASE.commit()

        gc.collect()

if __name__ == '__main__':
    Database.initialize()
    datafields = Allfields.fetchallfields()
    print (datafields)
