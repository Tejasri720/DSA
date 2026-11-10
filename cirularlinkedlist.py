#circular linked list
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter no.of nodes"))
for i in range(n):
    data=int(input("enter no. of nodes"))
    newnode=node(data)
    if head is None:
        head=newnode
        temp=head
    else:
        temp.next=newnode
        temp=newnode
if head is not None:
    temp.next=head
if head is None:
    print("Sll is empty")
else:
    temp=head
    while True:
        print(temp.data,end='->')
        temp=temp.next
        if temp==head:
            break
    print("Back to head")'''

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter no.of nodes"))
for i in range(n):
    data=int(input("enter no. of nodes"))
    newnode=node(data)
    if head is None:
        head=newnode
        temp=head
    else:
        temp.next=newnode
        temp=newnode
if head is not None:
    temp.next=head
if head is None:
    print("Sll is empty")
else:
    temp=head
    while True:
        print(temp.data,end='->')
        temp=temp.next
        if temp==head:
            break
    print("Back to head")
start=int(input("enter starting point"))
temp=head
while temp and temp.data !=start:
    temp=temp.next
    if temp==head:
        break
if temp is None or temp.data !=start:
    print("starting value not found!!!!!")
else:
    print("circular travesal")
    start_node=temp
    while True:
        print(temp.data,end='->')
        temp=temp.next
        if temp==start_node:
            break
    print("Back to head")