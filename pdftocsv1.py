# from PyPDF2 import PdfFileReader
# file=open('IPLmatch.pdf','rb')
# reader=PdfFileReader(file)
# num_pages=reader.numPages
# print(num_pages)
# for p in range(num_pages):
#     page=reader.getPage(p)
#     text=page.extractText()
#     print(text)
#     from googletrans import Translator
#     translator=Translator()
#     translate_text=translator.translate(text,dest='en')
#     print(translate_text)
# # #
# # #
# # #
# # #
# #
# # import deepl
# # auth_key = "YOUR_AUTH_KEY"
# # translator = deepl.Translator(auth_key)
# # translator.translate_document_from_filepath(
# #     "IPLmatch.pdf",
# #     "abcfileto.pdf",
# #     target_lang="EN-US"
# # )
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver import ActionChains
# import time
#
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 5)
# action = ActionChains(driver)
#
#
# driver.get("https://translate.google.co.in/")
#
# Document_btn = driver.find_element_by_xpath("IPLmatch.pdf")
# Document_btn.click()
# time.sleep(2)
#
# # Browse_Btn = driver.find_element_by_xpath("//*[@id='tlid-file-input']")
# # Browse_Btn.send_keys('Your Full File Path')
# # time.sleep(2)
#
# driver.find_element_by_xpath("//input[@value='Translate']").click()

import fitz
import json

document = fitz.open('IPLmatch.pdf')
page = document.load_page(0)  # enter page
text = page.get_text('dict')
# print(text)
import csv
with open('data.json', 'w') as f:
    text_data = json.dump(text, f)
# print(text_data)
x = open('data.json', encoding='utf-8')
data = json.load(x)
print(data)

# import pandas as pd
# print(pd.json_normalize(data))
# x.close()
# import pandas as pd
# df2 = pd.DataFrame.from_dict(data, orient="index")
# print(df2)
# df2.to_csv('IPLmatch.csv')
# fieldnames=["hello"]
# with open('test4.csv', 'w') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames =fieldnames )
#     writer.writeheader()
#     writer.writerows(data)
#
# f = csv.writer(open('IPLmatch.csv', 'w', encoding='utf-8', newline=''))
# for item in data:
#     f.writerow([item["text"]])