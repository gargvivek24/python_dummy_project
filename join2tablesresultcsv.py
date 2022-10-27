import time
start = time.time()
print(start)
import os
import mysql.connector
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("mysql+pymysql://root:root@localhost/mydatabase1")
engine.connect()
print(engine)



def fetch_table_data(filename,filename1):
    # The connect() constructor creates a connection to the MySQL server and returns a MySQLConnection object.
    cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='mydatabase1')
    cursor = cnx.cursor()
    query="select distinct Registration_number,Name,Admission_date,gender,percentage from "+filename
    print(query)
    query1=" join "+filename1+" on (Registration_number=REGISTRATIONNO)"
    query2=query+query1

    print(query2)
    cursor.execute(query2)

    header = [row[0] for row in cursor.description]

    rows = cursor.fetchall()

    # Closing connection
    cnx.close()

    return header, rows


def export(table_name,table_name2):
    header, rows = fetch_table_data(table_name,table_name2)
    column_name="joins"
    # Create csv file
    f = open(column_name + '.csv', 'w')

    # Write header
    f.write(','.join(header) + '\n')

    for row in rows:
        f.write(','.join(str(r) for r in row) + '\n')
    f.close()
    print(str(len(rows)) + ' rows written successfully to ' + f.name)


def function_name(data, data1):
    filename, extension = os.path.splitext(data)
    filename1, extension1 = os.path.splitext(data1)
    chunksize = 5000
    i = 0
    j = 1
    for data in pd.read_csv(data, chunksize=chunksize, iterator=True):
        data = data.rename(columns={c: c.replace(' ', '') for c in data.columns})
        data.index += j
        i = i + 1
        data.to_sql(filename, engine, if_exists='append')
        conn.commit()
        print("chunk  complete ", i)
        end = time.time()
        timetaken = end - start
        print(timetaken)

    i = 0
    j = 1
    for data in pd.read_csv(data1, chunksize=chunksize, iterator=True):
        data = data.rename(columns={c: c.replace(' ', '') for c in data.columns})
        data.index += j
        i = i + 1
        data.to_sql(filename1, engine, if_exists='append')
        conn.commit()
        print("chunk  complete ", i)
        end = time.time()
        timetaken = end - start
        print(timetaken)
    export(filename, filename1)


conn = engine.raw_connection()
function_name('Registration_details.csv', 'exam_results.csv')
conn.close()
end = time.time()
timetaken = end - start
print(timetaken)
