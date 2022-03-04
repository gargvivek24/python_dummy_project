import mysql.connector
import xlrd
import pandas as pd
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="mydatabase1"
)


f1 = pd.read_excel("Registration details.xlsx")
df = pd.DataFrame(f1)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Student (ADMISSION_DATE VARCHAR(20),Student_name VARCHAR(50),"
                 "Gender VARCHAR(10),DOB VARCHAR(20),Student_email_id VARCHAR(50),Enquiry_Number VARCHAR(50),"
                 "Registration_number VARCHAR(50))")
print("Table is created....")
for row in df:
    mycursor.execute(tuple('INSERT INTO Student(ADMISSION_DATE,Student_name,Gender,DOB,Student_email_id,Enquiry_Number,'
                     'Registration_number)''VALUES(%s, %s, %s, %s, %s, %s, %s)'), row)

mycursor.commit()

mycursor.close()
