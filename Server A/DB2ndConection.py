import mysql.connector


HOST = "mysql-2c36314c-mr-b049.aivencloud.com"
PORT = 19774
USER = "amiruhd"
PASSWORD = "AVNS_UuA7JoUFI9_DThIv7Ds"
DATABASE = "defaultdb"

mydb2 = mysql.connector.connect(
  host=HOST,
  port=PORT,
  user=USER,
  password=PASSWORD,
  database=DATABASE
)
mycursor2 = mydb2.cursor()

def ShowState(i):
    try:
        sql = "SELECT state FROM  Advertising WHERE id = %s"
        mycursor2.execute(sql, (i,))
        test = mycursor2.fetchone()
        mycursor2.reset()
        #print(test[0])
        return test[0]
    except():
        print("Unknown error in show state!")