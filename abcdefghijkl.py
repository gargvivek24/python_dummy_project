# # print("hello world")
# # print("hello world")
# # a = 10
# b="vivek"
# d=b[2:5]
# print(d)
# # c=a+b
# b=b.upper()
# print(b)
# # print(c)
# # if a == 10:
# #     print("hi")
# print("hello world")


a = {"a": [{"d":"nitin", "e":'vivek'}], "b": "world", "c": "hi"}
h=a.get('a')
print(h)
for item in h:
    e=item.get('e')
print(e)
# print(h)
# assert h=='hi',""