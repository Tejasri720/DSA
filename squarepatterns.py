#generate diagnoal and plus
n=int(input('enter'))
for i in range(n):  
    for j in range(n):
        if i==j or i+j==n-1 or i==n//2 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')

    print()

# generate plus
n=int(input('enter'))
for i in range(n):  
    for j in range(n):
        if i==n//2 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')

    print()
#generate plus in square
n=int(input('enter'))
for i in range(n):  
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 or i==n//2 or j==n//2 :
            print('*',end=' ')
        else:
            print(' ',end=' ')

    print()