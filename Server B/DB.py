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
    except():
        print("Error in set state!")

def Showstate(i):
    sql = "SELECT state FROM  Advertising WHERE id = %s"
    mycursor.execute(sql, (i,))
    test = mycursor.fetchone()
    mycursor.reset()
    return test[0]

def GetUrl(i):
    mycursor3 = mydb.cursor()
    sql = "SELECT ImageUrl, email FROM  Advertising WHERE id = %s"
    mycursor3.execute(sql, (i,))
    test = mycursor3.fetchone()
    url = test[0]
    em = test[1]
    mycursor3.reset()
    return test


def SetCategory(i, c):
    value = (c, i)
    if c == False:
        print()
    else:
        sql = "UPDATE Advertising SET Category = %s WHERE id = %s"
        mycursor.execute(sql, value)
        mydb.commit()
        mycursor.fetchone()
        mycursor.reset()