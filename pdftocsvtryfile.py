import tabula

import pandas as pd
# import camelot
# file = 'IPLmatch.pdf'
# tables = camelot.read_pdf(file, encoding='utf-8')
# df_p4 = tables[0].df
from googletrans import Translator
from tabula import read_pdf

# Read a PDF File

# import tabula
#
# # Read pdf into list of DataFrame
# df = tabula.read_pdf("IPLmatch.pdf", pages='all',encoding='UTF-8'
#                                                           )
# print(df)

# convert PDF into CSV file
# tabula.convert_into("IPLmatch.pdf", "IPLmatch.csv")
# from translate import Translator
# translator= Translator(from_lang="russian",to_lang="english")
# for line in df:
#     #translate the line instance and update the df
#     translation = translator.translate(line)


# import win_unicode_console
# # win_unicode_console.enable()
# tabula.convert_into("IPLmatch.pdf", "IPLmatch.csv")
# # list1 = []
# print(df)
# for item in df:
#     list1.append(item)
# df = pd.DataFrame(list1)
# df.to_excel('outputfile.xlsx', sheet_name='Sheet1', index=True)

# from pdfminer import high_level
#
# with open('IPLmatch.pdf', 'rb') as f:
#     text = high_level.extract_text(f)
#     print(text)
# translator = Translator()
#
# translations = translator.translate(df, dest='en')
# for translation in translations:  # print every translation
#
#     print(translation.text)
# # df = df.apply(lambda x: translator.translate(x, lang_tgt='en'))
# df = df.apply(lambda x: translator.translate(x, dest='en').text)
# print(df)
# print(translator.translate(myword, src='ru', dest='es').text)
# print(df)

# convert PDF into CSV

# df.to_csv('output.csv')

# print(df)


# import pdftables_api
#
# c = pdftables_api.Client('dozbi4v1x00q')
#
# c.csv('IPLmatch.pdf', 'IplMatch.csv')


import tabula
# Read a PDF File
df = tabula.read_pdf("IPLmatch.pdf", pages='all',encoding='KOI8-R')[0]
# convert PDF into CSV
tabula.convert_into("IPLmatch.pdf", "iplmatch.csv", output_format="csv", pages='all')
print(df)