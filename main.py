#write a program to add the digits of a givin number
n=int(input("enter a number"))
s=0
while n!=0:
    d=n%10
    s+=d
    n//=10
print('sum:',s)
