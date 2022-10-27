import mysql.connector
import sqlalchemy

import os
import pandas as pd

from sqlalchemy import create_engine


# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root",
#   database="mydatabase1"
# )
engine = create_engine("mysql+pymysql://root:root@localhost/mydatabase1")
engine.connect()
print(engine)

result=[]
def function_name(data,data1):
    filename, extension = os.path.splitext(data)
    filename1, extension1 = os.path.splitext(data1)
    # data1='fivem_records'
    chunksize = 50000
    i = 0
    j = 1
    for data in pd.read_csv(data, chunksize=chunksize, iterator=True):
        data = data.rename(columns={c: c.replace(' ', '') for c in data.columns})
        data.index += j
        i=i+1
        data.to_sql(filename, engine, if_exists='append')
        # j = data.index[-1] + 1
        conn.commit()
        print("chunk  complete ",i)



  # data_frame = data.to_sql('Student5', engine, method='multi', index=False,
  #                          if_exists='append')
  #print(data_frame)


conn = engine.raw_connection()
function_name('Registration_details.csv','exam_results.csv')
# function_name('exam_results.csv')


conn.close()
# end = time.time()
# timetaken=end-start
# print(timetaken)
# df=pd.read_csv('')
# df.to_sql("Student",con=mydb,if_exists="append",index=False)

