import mysql.connector


HOST = "mysql-2c36314c-mr-b049.aivencloud.com"
PORT = 19774
USER = "amiruhd"
PASSWORD = "AVNS_UuA7JoUFI9_DThIv7Ds"
DATABASE = "defaultdb"

mydb = mysql.connector.connect(
  host=HOST,
  port=PORT,
  user=USER,
  password=PASSWORD,
  database=DATABASE
)
mycursor = mydb.cursor()

def getid(d):
    sql = "SELECT id FROM  Advertising WHERE description_ = %s"
    mycursor.execute(sql, (d,))
    test = mycursor.fetchone()
    print(test[0])
    mycursor.reset()
    return test[0]

def setstate(id, b):
    value = id
    try:
        if b:
            sql = "UPDATE Advertising SET state = 'Accepted' WHERE id = %s"
        else:
            sql = "UPDATE Advertising SET state = 'Rejected' WHERE id = %s"
        mycursor.execute(sql, (value,))
        mydb.commit()
        mycursor.fetchone()
        mycursor.reset()
    except e:
        print("Error in set state!")