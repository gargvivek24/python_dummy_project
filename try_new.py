import configparser, os
import glob
import shutil

# Get the current working directory
cwd = os.getcwd()

# Print the current working directory
print("Current working directory: {0}".format(cwd))
current_file=os.path.basename(__file__)
print(current_file)
current_file1=cwd+"\\"
current_file2=current_file1+current_file
print(current_file2)



path = "C:\\Users\\dell\\PycharmProjects"
configfilepath = glob.glob(path + "/**/config.ini", recursive = True)
print(configfilepath)
a=configfilepath[0]
print(a)
head1,tail1= os.path.split(a)
print(head1)
head2=head1+'\\'
print(head2)
current_file=os.path.basename(__file__)
print(current_file)
completeName = os.path.join(head2, current_file)
print(completeName)
# absolute path
dst_path = r"E:\pynative\account\sales.txt"
shutil.copy(current_file2, head2)




#
#
# config = configparser.ConfigParser()
# a=config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
# print(a)
#
# def listToString(s):
#     # initialize an empty string
#     str1 = ""
#
#     # return string
#     return (str1.join(s))
# b=listToString(a)
# head1,tail1= os.path.split(b)
# print(head1)
# head2=head1+'\\'
# print(head2)
# print(tail1)
# current_file=os.path.basename(__file__)
# print(current_file)
# completeName = os.path.join(head2, current_file)
# print(completeName)
# file = open(completeName,'a')
# file.write('print("Blah Blah")')
# file.close()
# print("Blah Blah")