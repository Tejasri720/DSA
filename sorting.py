#bubble sort
'''arr=list(map(int,input("enter elements").split()))
n=len(arr)
for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(*arr)


#selection sort
arr=list(map(int,input("enter elements").split()))
n=len(arr)
for i in range(n):
    minindex=i
    for j in range(i+1,n):
        if arr[j]<arr[minindex]:
            minindex=j
    arr[i],arr[minindex]=arr[minindex],arr[i]
print(*arr)


#insertion sort
arr=list(map(int,input('enter elements').split()))
n=len(arr)
for i in range(n):
    x=arr[i]
    j=i-1
    while j>=0 and arr[j]>x:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=x
print(*arr)


#merge sort
def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=mergesort(arr[:mid])
    right=mergesort(arr[mid:])
    result=[]
    while left and right:
        if left[0]<right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result+left+right
arr=list(map(int,input('enter elements').split()))
print(mergesort(arr))


#flip or pancakesort
def pancakesort(arr):
     n=len(arr)
     for size in range(n,1,-1):
          max_index=arr.index(max(arr[:size]))
          arr[:max_index+1]=arr[:max_index+1][::-1]
    return arr
arr=list(map(int,input('enter elements').split()))
print("sorted array:",pancakesort(arr))'''


#Quick sort
'''def quicksort(arr):
    n=len(arr)
    if n<=1:
        return arr
    pivot=arr[-1]
    left=[x for x in arr[:-1] if x<=pivot]
    right=[x for x in arr[:-1] if x>pivot]
    return quicksort(left)+[pivot]+quicksort(right)l
arr=list(map(int,input('enter the elements').split()))
print('sorted array:',quicksort(arr))


#Transversal of an array
n=int(input("Enter the size of the matrix:"))
arr=[[0]* n for _ in range(n)]
print(arr)
top=0
bottom=n-1
left=0
right=n-1
num=1
while top<=bottom and left<=right:
    #top, from left to right
    for i in range(left,right+1):
        arr[top][i]=num
        num+=1
    top+=1
    #right, from top to bottom
    for i in range(top,bottom+1):
        arr[i][right]=num
        num+=1
    right-=1
    #bottom, right to left
    for i in range(right,left-1,-1):
        arr[bottom][i]=num
        num+=1
    bottom-=1
    #left, bottom to top
    for i in range(bottom,top-1,-1):
        arr[i][left]=num
        num+=1
    left+=1
for row in arr:
    for x in row:
        print(f"{x:4}",end='')
    print()




n=int(input("Enter the size of the matrix:"))
arr=[]
for i  in range(n):
    arr.append(list(map(int,input("enter numbers").split())))
top=0
bottom=n-1
left=0
right=n-1
while top<=bottom and left<=right:
    #top, from left to right
    for i in range(left,right+1):
        print(arr[top][i],end=' ')
        
    top+=1
    #right, from top to bottom
    for i in range(top,bottom+1):
        print(arr[i][right],end=' ')
        
    right-=1
    #bottom, right to left
    for i in range(right,left-1,-1):
        print(arr[bottom][i],end=' ')
        
    bottom-=1
    #left, bottom to top
    for i in range(bottom,top-1,-1): 
        print(arr[i][left],end=' ')
        
    left+=1'''
