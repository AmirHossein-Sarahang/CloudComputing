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

def getid(i):
    mycursor2 = mydb.cursor()
    sql2 = "SELECT email FROM  Advertising WHERE id = %s"
    mycursor2.execute(sql2, (i,))
    test = mycursor2.fetchone()
    print(test[0])
    return test[0]