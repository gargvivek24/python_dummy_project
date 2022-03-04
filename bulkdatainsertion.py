import time
start = time.time()
print(start)
import csv
import mysql.connector

connection = mysql.connector.connect(user='root', password='root', host='localhost',database='mydatabase1')
mycursor = connection.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Student (ADMISSION_DATE VARCHAR(20),Student_name VARCHAR(50),"
                 "Gender VARCHAR(10),DOB VARCHAR(20),Student_email_id VARCHAR(50),Enquiry_Number VARCHAR(50),"
                 "Registration_number VARCHAR(50))")
print("Table is created....")


def insert_Registeration():
    with open('fiftythourec1.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        next(spamreader)
        for row in spamreader:
            # Prepare SQL query to INSERT a record into the database.
            sql = "INSERT INTO Student (ADMISSION_DATE, Student_name, Gender, DOB, Student_email_id, Enquiry_Number, Registration_number) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s' );" % (row[0], row[1], row[2],row[3],row[4],row[5],row[6])
            # print(sql)
            try:
               # Execute the SQL command
               mycursor.execute(sql)
               connection.commit()

            except:
               # Rollback in case there is any error
               connection.rollback()
# Commit your changes in the database

insert_Registeration()

mycursor.close()
end = time.time()
timetaken=end-start
print(timetaken)