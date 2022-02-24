import configparser, os
config = configparser.ConfigParser()
a=config.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
print(a)

def listToString(s):
    # initialize an empty string
    str1 = ""

    # return string
    return (str1.join(s))
b=listToString(a)
head1,tail1= os.path.split(b)
print(head1)
head2=head1+'\\'
print(head2)
print(tail1)
current_file=os.path.basename(__file__)
print(current_file)
completeName = os.path.join(head2, current_file)
print(completeName)
