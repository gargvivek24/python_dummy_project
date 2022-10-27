import pandas as pd
import glob

path = "C:\\Users\\dell\\PycharmProjects\\pythonProject2\\input"

# read all the files with extension .xlsx i.e. excel
filenames = glob.glob(path + "\*.xlsx")
print('File names:', filenames)
for f in filenames:
    # read the csv file
    df = pd.read_excel(f)
    print('Location:', f)
    print(df)
    print('File Name:', f.split("\\")[-1])

    # print the content
    # print('Content:')
    # print(df)
