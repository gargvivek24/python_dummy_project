# # import pandas as pd
# # import glob
# #
# # # getting excel files to be merged from the Desktop
# # path = "C:\\Users\\dell\\PycharmProjects\\pythonProject2\\input"
# #
# # # read all the files with extension .xlsx i.e. excel
# # filenames = glob.glob(path + "\*.xlsx")
# # print('File names:', filenames)
# #
# # # empty data frame for the new output excel file with the merged excel files
# # outputxlsx = pd.DataFrame()
# #
# # # for loop to iterate all excel files
# # for file in filenames:
# #    # using concat for excel files
# #    # after reading them with read_excel()
# #    df = pd.concat(pd.read_excel( file, sheet_name=None), ignore_index=True, sort=False)
# #
# #    # appending data of excel files
# #    outputxlsx = outputxlsx.append( df, ignore_index=True)
# #    outputxlsx=outputxlsx.drop_duplicates()
# # print('Final Excel sheet now generated at the same location:')
# # outputxlsx.to_excel("C:\\Users\\dell\\PycharmProjects\\pythonProject2\\output\\Output.xlsx", index=False)
#
#
# def _get_transformed_value(self, document):
#    """
#    Checks is_self_canonical column in deepcrawl data.
#    Returns 0 if missing or False. Else 1.
#    """
#    is_self_canonical_url = self.DEFAULT_VALUE
#    url = document['url']
#    canonical_url = document["canonical_url"]
#    if canonical_url not in IGNORE_VALUES:
#       is_self_canonical_url = True if url in canonical_url else False
#    if is_self_canonical_url is False:
#       # probability we have a non self canonical url or we received only path.
#       absolute_url_list = self._get_absolute_url_list(url, canonical_url)
#       is_self_canonical_url = True if url in absolute_url_list else False
#    return is_self_canonical_url
#
#
# @staticmethod
# def _get_absolute_url_list(main_url, url_list):
#    parsed_uri = urlparse(main_url)
#    new_list = []
#    main_domain = '%s://%s' % (parsed_uri.scheme, parsed_uri.netloc)
#    for url in url_list:
#       if (url not in IGNORE_VALUES) and (url != ''):
#          parse_comps = urlparse(url)
#          # only path given
#          if parse_comps.scheme in IGNORE_VALUES and parse_comps.netloc in IGNORE_VALUES and parse_comps.path:
#             new_list.append(''.join([main_domain, url]))
#    return new_list
#
#
# url = "https://www.capitalone.com/credit-cards/students/"
# canonical_url = "https://www.capitalone.com/credit-cards/students/"
# if canonical_url not in '':
#    is_self_canonical_url = True if url in canonical_url else False
#    print(is_self_canonical_url)Kha hai? Call utha jldi
#    # if is_self_canonical_url is False:
#       # probability we have a non self canonical url or we received only path.
#       # absolute_url_list = self._get_absolute_url_list(url, canonical_url)
import time
import pywhatkit as pwt
import pyautogui as pg
pwt.sendwhatmsg("+9100000000000", "Hello", 11,00)
time.sleep(5)
pg.press('Enter')








#       # is_self_canonical_url = True if url in absolute_url_list else False
#    # return is_self_canonical_url
