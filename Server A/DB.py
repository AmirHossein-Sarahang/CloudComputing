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
    valus= (d, e, s, c)
    mycursor.execute(sql, valus)
    mydb.commit()

#sql = "INSERT INTO Advertising (description_, email, state, category) values (%s, %s, %s, %s)"
#val = ("Michelle", "Blue Village", "Dsfds", "dsfsd")
#mycursor.execute(sql, val)
#mydb.commit()
print(mydb)

#mycursor.execute("SHOW TABLES")
#insert("aaa", "sdf", "asd", "asd")

#mycursor.execute("SELECT * FROM  Advertising")

#sql = "DELETE FROM Advertising WHERE id = '1'"
#mycursor.execute(sql)
#mydb.commit()

#for x in mycursor:
#    print(x)
