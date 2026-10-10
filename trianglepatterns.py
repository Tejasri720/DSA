#left sided right angle triangle
n=int(input('enter'))
for i in range(n):  
    for j in range(n):
        if  i==n-1 or j==0 or i==j :
            print('*',end=' ')
        else:
            print(' ',end=' ')

    print()


#inverted right angle triangle
n=int(input('enter'))
for i in range(n):  
    for j in range(n):
        if i==0   or j==n-1 or i==j :
            print('*',end=' ')
        else:
            print(' ',end=' ')

    print()

#right sided right angle triangle
n=int(input('enter'))
for i in range(n):  
    for j in range(n):
        if  i==n-1  or j==n-1 or  i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')

    print()


#inverted triangle
n=int(input('enter'))
for i in range(n):  
    for j in range(n):
        if i==0  or j==0 or  i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')

    print()