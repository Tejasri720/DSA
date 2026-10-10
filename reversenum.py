#write a program to reverse a number
n=int(input('enter the number'))
rev=0
while n!=0:
    d=n%10
    rev=rev*10+d
    n//=10
print(rev)


#write a program to reverse a number
n=int(input("\n Enter a number"))
while n!=0:
    d=n%10
    print(d,end='')
    n//=10