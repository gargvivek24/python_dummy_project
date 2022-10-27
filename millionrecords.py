import time
start = time.time()
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


def function_name():

  data = pd.read_csv('millionsalesrecord.csv')
  data_frame = data.to_sql('Student3', engine, method='multi', index=False,
                           if_exists='replace')
  data_frame.commit()
conn = engine.raw_connection()
function_name()


conn.close()
end = time.time()
timetaken=end-start
print(timetaken)
