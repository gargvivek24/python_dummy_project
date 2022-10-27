import time

import pandas as pd
from sqlalchemy import create_engine
engine = create_engine("mysql+pymysql://root:root@localhost/mydatabase1")
engine.connect()
result = []
def function_name():
    data = 'Regi'
    chunksize = 50000
    i = 0
    j = 1
    for data in pd.read_csv(data, chunksize=chunksize, iterator=True):
        data = data.rename(columns={c: c.replace(' ', '') for c in data.columns})
        data.index += j
        i = i + 1
        data.to_sql('student', engine, if_exists='append')
        # j = data.index[-1] + 1
        conn.commit()
        print("chunk  complete ", i)


conn = engine.raw_connection()
function_name()
conn.close()


