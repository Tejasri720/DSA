#generate odd numbers
n=int(input("enter the number"))
for i in range(1,n+1):
    if i%2==1:
        print(i ,end=' ')