import pandas as pd

file1 = pd.read_excel("C:\\Users\\dell\\PycharmProjects\\pythonProject2\\input\\cars1.xlsx")
file2 = pd.read_excel("C:\\Users\\dell\\PycharmProjects\\pythonProject2\\input\\cars2.xlsx")

file3 = pd.merge(file1,file2 , on='id', how="outer")

file3.to_excel("C:\\Users\\dell\\PycharmProjects\\pythonProject2\\output\\merged.xlsx",index=False)