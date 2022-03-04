import pandas

# reading the files
f1 = pandas.read_excel("Registration details.xlsx")
f2 = pandas.read_excel("exam results.xlsx")

# merging the files
f3 = f1[["REGISTRATION NO",
         "STUDENT EMAIL ID "]].merge(f2[["REGISTRATION NO",
                                         "Name", "Marks Obtained",
                                         "Percentage"]],
                                     on="REGISTRATION NO",
                                     how="right")

# creating a new file
f3.to_excel("Results1.xlsx", index=False)