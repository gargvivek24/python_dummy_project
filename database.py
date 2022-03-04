import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="mydatabase1"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS customers5 (name VARCHAR(255), address VARCHAR(255))")
# sql = "INSERT INTO customers4 (name, address) VALUES (%s, %s)"
# sql = "INSERT INTO customers4 (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]
#
# mycursor.executemany(sql, val)
# mydb.commit()
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
# mydb.commit()
# mycursor.execute("SELECT * FROM customers4")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)
# mycursor.execute("SELECT name FROM customers4")
#
# myresult = mycursor.fetchall()
#
# for x in myresult:
#   print(x)
# mycursor.execute("select * from customers")

#
#
# mycursor.execute("SHOW DATABASES")
# for x in mycursor:
#   print(x)
mycursor.execute("SELECT * FROM customers4")

myresult=mycursor.fetchone()
print(myresult)
print("hello")
# myresult=mycursor.fetchone()
# print(myresult)
myresult=mycursor.first()

myresult = mycursor.fetchall()
for x in myresult:
  print(x)


