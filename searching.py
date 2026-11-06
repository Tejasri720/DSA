#1-d array searching
'''arr=list(map(int,input('enter').split()))
search=int(input('enter seach element'))
found=False
for i in range(len(arr)):
    if arr[i]==search:
        print('element found at',i)
        found=True
        break
if not found:
    print('element not found ')

# searching an element at n-dimentionally
n=int(input('enter the size'))
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
search=int(input('enter element to be searched:'))
found=False
for i in range(n):
    for j in range(n):
        if arr[i][j]==search:
            print('element found at row:',i,"col:",j)
            found=True
            break
if not found:
    print("element out of range")


# adding of matrix
n=int(input('enter the size'))
arr=[]
s=0
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        s+=arr[i][j]
print("Total:",s)

#induvidual row adding
n=int(input('enter the size'))
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    s=0
    for j in range(n):
        s+=arr[i][j]
    print('row:',i+1,"sum:",s)

#induvidual column adding
n=int(input('enter the size'))
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
for j in range(n):
    s=0
    for i in range(n):
        s+=arr[i][j]
    print('col:',j+1,"sum:",s)

#diagnoal and anti diagnoal  sum
n=int(input('enter the size'))
arr=[]
di=0
ad=0
for i in range(n):
    arr.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if i==j:
           di+=arr[i][j]
        if i+j==n-1:
           ad+=arr[i][j]
print('diagnoal','sum:',di)
print('antidiagnoal','sum:',ad)


#Binary search
arr=list(map(int,input("enter elements").split()))
arr.sort()
val=int(input("enter a element to search"))
low=0
high=len(arr)-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]==val:
        print('element fount at',mid)
        break
    elif arr[mid]<val:
        low=mid+1
    else:
        high=mid-1
else:
    print('element not found')'''


#find the square root of a number using binary search
val=int(input("enter a element"))
low=0
high=val
while low<=high:
    mid=(low+high)//2
    if mid*mid==val:
        print('square root:',mid)
        break
    elif mid*mid<val:
        low=mid+1
    else:
        high=mid-1
else:
    print('integer square root ',high)