
# print("Enter how many times you wish to run the program")
# a= int(input())
# n = 0
# for i in range(a):
#     print("Enter the value of x,y,z")
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     for j in range(z):
#         m = x + y
#         if j == 0:
#             print(m, end=" ")
#         else:
#             m = n + x + 2 ** j * y
#             print(m, end=" ")
#             n = m - x
#         n = m - x
#     print()

list=[1,2,3,4,5,6,8.0,0.0,.0]
for i in range(len(list)):
    print(type(list[i]))
    if type(list[i] is int):
        print("hello1")
        list[i]=int(list[i])
    elif type(list[i] is float):
        print("hello")
        list[i] = float(list[i])
print(list)
# for item in list:
#     print(type(item))
# print(sorted(list))
