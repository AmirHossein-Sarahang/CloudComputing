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

def Insert(d, e, u):
    try:
        sql = "INSERT INTO Advertising (description_, email, state, ImageUrl) values (%s, %s, %s, %s)"
        valus = (d, e, "Pending", u)
        mycursor.execute(sql, valus)
        mydb.commit()
        mycursor.reset()
        return getid(d)
    except():
        print("Error registering information! please try again later")


def Get_id(d):
    try:
        sql = "SELECT id FROM  Advertising WHERE description_ = %s"
        mycursor.execute(sql, (d,))
        test = mycursor.fetchone()
        mycursor.reset()
        return test[0]
    except():
        print("Unknown error in returning ID!")


def show_all_tables():
    try:
        mycursor.execute("SELECT * FROM Advertising")
        t = mycursor.fetchall()
        mycursor.reset()
        for x in t:
            print(x)
    except():
        print("Unknown error in show_all_tables!")


def showstate(i):
    try:
        sql = "SELECT state FROM  Advertising WHERE id = %s"
        mycursor.execute(sql, (i,))
        test = mycursor.fetchone()
        mycursor.reset
        print(test[0])
        return test[0]
    except():
        print("Unknown error in show state!")