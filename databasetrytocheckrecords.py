import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="mydatabase1"
)
mycursor = mydb.cursor()
# mycursor.execute("select CASE WHEN Student_email_id=Student_email_id THEN" lstrip('Student_email_id','0') "ELSE" lstrip('Student_email_id,'0') "END from student")
mycursor.execute("select CASE WHEN Student_email_id=Student_email_id THEN " "lstrip('Student_email_id','0')" " ELSE" " lstrip('Student_email_id,'0')" " END from student")

# myresult = mycursor.fetchall()
# for x in myresult:
#   print(x)