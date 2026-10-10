#gerenrate diagnol
n=int(input('enter'))
for i in range(n):  
    for j in range(n):
        if i==j or i+j==n-1 :
            print('*',end=' ')
        else:
            print(' ',end=' ')

    print()


# generate diagnoal in a hollow square
n=int(input('enter'))
for i in range(n):  
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==j or  i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')

    print()

# generate  timer pattern
n=int(input('enter'))
for i in range(n):  
    for j in range(n):
        if i==0 or i==j or i==n-1 or  i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')

    print()

#generate butterfly pattern
n=int(input('enter'))
for i in range(n):  
    for j in range(n):
        if  j==0 or j==n-1 or i==j or  i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')

    print()

