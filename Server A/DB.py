import mysql.connector


HOST = ""
PORT = 19774
USER = ""
PASSWORD ""
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
        return Get_id(d)
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


def ShowAllTables():
    try:
        mycursor.execute("SELECT * FROM Advertising")
        t = mycursor.fetchall()
        mycursor.reset()
        for x in t:
            print(x)
    except():
        print("Unknown error in show_all_tables!")


