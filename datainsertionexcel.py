import csv
import mysql.connector

connection = mysql.connector.connect(user='root', password='root', host='localhost',database='mydatabase1')
mycursor = connection.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Student (ADMISSION_DATE VARCHAR(20),Student_name VARCHAR(50),"
                 "Gender VARCHAR(10),DOB VARCHAR(20),Student_email_id VARCHAR(50),Enquiry_Number VARCHAR(50),"
                 "Registration_number VARCHAR(50))")
print("Table is created....")
def insert_Registeration():
    with open('Registration_details.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        columns =next(spamreader)
        query = 'insert into Student({0}) values ({1})'
        query = query.format(','.join(columns), ','.join('?' * len(columns)))
        cursor = connection.cursor()
        for data in spamreader:
            mycursor.execute(query, data)
            mycursor.commit()
insert_Registeration()
mycursor.close()