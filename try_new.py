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




