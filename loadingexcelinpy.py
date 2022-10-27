import pymysql
import pandas as pd

con = pymysql.connect(host = 'localhost', user = 'root', passwd = 'root', db = 'mydatabase1')

cursor = con.cursor()
# cursor = database.cursor()
sheet = pd.read_csv("Registration_details.csv")
#sheet = df.sheet_by_name("Registration_details")
query ="""INSERT INTO Student(ADMISSION_DATE, Student_name, Gender, DOB, Student_email_id, Enquiry_Number, Registration_number) VALUES(%s, %s, %s, %s, %s, %s, %s)"""

for r in range(1, len(sheet.index)):
	    ADMISSION_DATE		= sheet.head1(r,).value
	    Student_name	= sheet.head2(r,1).value
	    Gender			= sheet.c(r,2).value
	    DOB		= sheet.cell(r,3).value
	    Student_email_id		= sheet.cell(r,4).value
	    Enquiry_Number	= sheet.cell(r,5).value
	    Registration_number		= sheet.cell(r,6).value
    	#values = (ADMISSION_DATE, Student_name, Gender, DOB, Student_email_id, Enquiry_Number, Registration_number)
    	#cursor.execute(query, values)
cursor.close()

# Commit the transaction
con.commit()

# Close the database connection
con.close()
print("")
print("All Done! Bye, for now.")
print("")
columns = str(sheet.ncols)
rows = str(sheet.nrows)

