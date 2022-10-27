import time

start = time.time()
print(start)
import mysql.connector


def fetch_table_data(table_name):
    # The connect() constructor creates a connection to the MySQL server and returns a MySQLConnection object.
    cnx = mysql.connector.connect(user='root', password='root', host='localhost', database='mydatabase1')

    cursor = cnx.cursor()
    query = "select REGISTRATION NO,STUDENT EMAIL ID from " + table_name
    print(query)
    query1 = " where  OrderID='170386207'"
    query2 = query + query1
    print(query2)
    cursor.execute("select ORDERId from " + table_name + " where  OrderID>'1000'")

    header = [row[0] for row in cursor.description]

    rows = cursor.fetchall()

    # Closing connection
    cnx.close()

    return header, rows


def export(table_name):
    header, rows = fetch_table_data(table_name)
    column_name = "ItemType"
    # Create csv file
    f = open(column_name + '.csv', 'w')

    # Write header
    f.write(','.join(header) + '\n')

    for row in rows:
        f.write(','.join(str(r) for r in row) + '\n')

    f.close()
    print(str(len(rows)) + ' rows written successfully to ' + f.name)


# Tables to be exported
# export('customers4')
export('student')
end = time.time()
time_taken = end - start
print(time_taken)
