# assert sum([1,2, 3, 4]) == 10, "Should be 10"
# # print("hello")
#
#
# # def test_sum2():
# #     assert sum([2, 3, 5]) == 10, "It should be 10"
# #
# #
# # def test_sum_tuple():
# #     assert sum((2, 4, 5)) == 10, "It should be 10"
# #
# # test_sum2()
# # test_sum_tuple()
# # print("Everything is correct")
#
# def test_sum_tuple1():
#     assert sum((2, 3, 5)) == 10,"It should be 10"
#     print("hello")
# try:
#     test_sum_tuple1()
# except AssertionError as msg:
#     print(msg)

import re

# initializing string
test_string = "There are 24 apples for 4 persons"

# printing original string
print("The original string : " + test_string)

# using re.findall()
# getting numbers from string
temp = re.findall(r'\d+', test_string)
res = list(map(int, temp))

# print result
print(f"The numbers list is : {res[0]}")

