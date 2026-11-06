#second largest
'''arr=list(map(int,input("enter numbers").split()))
if len(arr)<2:
    print("Not enough elements")
else:
    largest=float('-inf')
    second=float('-inf')
    for val in arr:
        if val>largest:
            second=largest
            largest=val
        elif val>second and val !=largest:
            second=val
    if second==float('-inf'):
        print("No second number")
    else:
        print('second number',second)


#tom riddle anagram
s1=input().lower()
s2=input().lower()
s1=s1.replace(" ","")
s2=s2.replace(" ","")
s1=''.join(ch for ch in s1 if ch.isalpha())
s2=''.join(ch for ch in s2 if ch.isalpha())
if len(s1)==0 or len(s2)==0:
    print('not tom riddle anagram')
elif len(s1)==1 or len(s2)==0:
    print('Not an  tom riddle anagram')
elif len(s1)!=len(s2):
     print("not tom riddle anagram")
elif len(set(s1))== 1 or len(set(s2))==1:
    print("not tom riddle anagram")
elif sorted(s1)==sorted(s2):
        print('tom riddle anagram')
else:
    print("not")


#search n a rotated for array

arr=list(map(int,input("enter elements").split()))
search=int(input("enter a value to be searched:"))
low=0
high=len(arr)-1
ans=-1
while low<= high:
    mid=(low+high)//2
    if arr[mid]==search:
        ans=mid
        break
    if arr[low]<=arr[mid]:
        if arr[low]<=search<=arr[mid]:
            high=mid-1
        else:
            low=mid+1
    else:
        if arr[mid]<search<=arr[high]:
            low=mid+1
        else:
            high=mid-1
print(ans)

#finding the first occurrence of a mumber

arr=list(map(int,input("enter elements").split()))
num=int(input("enter the vale to be searches"))
low=0
high=len(arr)-1
ans=-1
while low<=high:
    mid =(low+high)//2
    if arr[mid]==num:
        ans=mid
        high=mid-1
    elif arr[mid]<num:
        low=mid+1
    else:
        high=mid+1
print("lowes occurrence index:",ans)


#finding the last occurrence of a number

arr=list(map(int,input("enter elements").split()))
num=int(input("enter the vale to be searches:"))
low=0
high=len(arr)-1
ans=-1
while low<=high:
    mid =(low+high)//2
    if arr[mid]==num:
        ans=mid
        low=mid+1
    elif arr[mid]<num:
        low=mid+1
    else:
        high=mid-1
print("Highest occurrence index:",ans)

#find the count occurrence  of a numbers 

arr=list(map(int,input("enter elements").split()))  
num=int(input("enter the vale to be searches:"))
low=0
high=len(arr)-1
first ,last=-1,-1
while low<=high:
    mid =(low+high)//2
    if arr[mid]>=num:
        if arr[mid]==num:
            first=mid
        high=mid-1
    else:
        low=mid+1
low=0
high=len(arr)-1
while low<=high:
    mid=(low+high)//2
    if arr[mid]<=num:
        if arr[mid]==num:
            last=mid
        low=mid+1
    else:
        high=mid-1
print(last-first+1 if first !=-1 else 0)'''




