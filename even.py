#generate n even  numbers
n=int(input("enter n:"))
i=1
while i<=n:
    if i%2==0:
        print(i,end=' ')
    i+=1