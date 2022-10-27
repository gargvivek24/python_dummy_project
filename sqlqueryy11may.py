from pandas import *
import pandas as pd
CSV_DATA = read_csv('patient.csv')
my_columns = CSV_DATA[["id","visit_date","people" ]]
rslt_df = my_columns[my_columns['people'] >=100 ]
rows = my_columns.shape[0]
outputxlsx = pd.DataFrame()
i=0
for i in range(rows):
    row_df = my_columns.iloc[i:i+1]
    abc=my_columns.iloc[i:i+1]['people'] >=100
    abc=abc.to_string(index=False)

    if abc=='True':

        bcd = my_columns.iloc[i+1:i + 2]['people'] >= 100
        bcd = bcd.to_string(index=False)
        if bcd=='True':

            xyz=my_columns.iloc[i+2:i + 3]['people'] >= 100
            xyz = xyz.to_string(index=False)
            if xyz=='True':

                df=my_columns.iloc[i:i+1]
                outputxlsx = outputxlsx.append(df, ignore_index=True)
                df1=my_columns.iloc[i+1:i+2]
                outputxlsx = outputxlsx.append(df1, ignore_index=True)
                df2=my_columns.iloc[i+2:i+3]
                outputxlsx = outputxlsx.append(df2, ignore_index=True)
                outputxlsx = outputxlsx.drop_duplicates()

outputxlsx.to_excel("C:\\Users\\dell\\PycharmProjects\\pythonProject2\\output\\Output.xlsx", index=False)