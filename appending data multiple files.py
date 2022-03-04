import pandas as pd
import glob

# getting excel files to be merged from the Desktop
path = "C:\\Users\\dell\\PycharmProjects\\pythonProject2\\input"

# read all the files with extension .xlsx i.e. excel
file_list = glob.glob(path + "\*.xlsx")
print(file_list)

excl_list = []

for file in excl_list:
    excl_list.append(pd.read_excel(file))

# concatenate all DataFrames in the list
# into a single DataFrame, returns new
# DataFrame.
excl_merged = pd.concat(excl_list, ignore_index=True)

# exports the dataframe into excel file
# with specified name.
excl_merged.to_excel('C:\\Users\\dell\\PycharmProjects\\pythonProject2\\output\\Output.xlsx', index=False)