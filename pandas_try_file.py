import pandas as pd
df = pd.read_excel (r'C:\\Users\\dell\\Desktop\\pythontry.xlsx')
print (df)
df.iloc[:,0]
df.iloc[:,-1]
import pandas as pd

df = pd.read_excel (r'C:\\Users\\dell\\Desktop\\pythontry.xlsx')
#print (df)
#df.name
# df.name.count()
# #print(new_header)
# # df1 = pd.read_excel (r'C:\\Users\\dell\\Desktop\\pythontry.xlsx')
# # print(df1)
# # print(df.iloc[:,1])
# # print(df1.iloc[:,-1])
# #result = df.sort_values('id')
# #print(result)
# df.shape
# df.to_excel('input file.xlsx')
# df[['id','phone']].to_excel('output.xlsx',index = False)
# df.sort_values(['id'])[:].to_excel('output1.xlsx',index = False)
df.to_csv('saved1_file.csv',index= False)
df.sort_values(['id'])[:].to_csv('output2.csv',index = False)
df[df.name.str.startswith('d')].to_csv('output2.csv',index = False)