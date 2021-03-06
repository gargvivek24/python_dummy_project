import pandas as pd
import glob

# getting excel files to be merged from the Desktop
path = "C:\\Users\\dell\\PycharmProjects\\pythonProject2\\input"

# read all the files with extension .xlsx i.e. excel
filenames = glob.glob(path + "\*.xlsx")
print('File names:', filenames)

# empty data frame for the new output excel file with the merged excel files
outputxlsx = pd.DataFrame()

# for loop to iterate all excel files
for file in filenames:
   # using concat for excel files
   # after reading them with read_excel()
   df = pd.concat(pd.read_excel( file, sheet_name=None), ignore_index=True, sort=False)

   # appending data of excel files
   outputxlsx = outputxlsx.append( df, ignore_index=True)
   outputxlsx=outputxlsx.drop_duplicates()
print('Final Excel sheet now generated...')
outputxlsx.to_excel("C:\\Users\\dell\\PycharmProjects\\pythonProject2\\output\\Output.xlsx", index=False)
