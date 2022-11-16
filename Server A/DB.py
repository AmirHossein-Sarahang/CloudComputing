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

def insert(d, e, s, c):
    sql = "INSERT INTO Advertising (description_, email, state, category) values (%s, %s, %s, %s)"
    valus = (d, e, s, c)
    mycursor.execute(sql, valus)
    mydb.commit()
    getid(d)


def getid(d):
    mycursor2 = mydb.cursor()
    sql2 = "SELECT id FROM  Advertising WHERE description_ = %s"
    mycursor2.execute(sql2, (d,))
    test = mycursor2.fetchone()
    print(test[0])
    return test[0]

def show_all_tables():
    mycursor3 = mydb.cursor()
    mycursor3.execute("SELECT * FROM Advertising")
    t = mycursor3.fetchall()
    for x in t:
        print(x)