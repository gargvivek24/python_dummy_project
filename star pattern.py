i=0

j=5
for i in range(6):

    for k in range(5-i):
        print(' ', end='')
    for j in range(i):
        print('*',end='')
    print()

