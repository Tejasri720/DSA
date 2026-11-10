'''#1.DoubleLinkedlist at begining
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("Enter number of nodes"))
for i in range(n):
    data=int(input("Enter the value:"))
    newnode=node(data)
    newnode.next=head
    if head is not None:
        head.prev=newnode
    head=newnode
print("DLL:")
temp=head
while temp:
    print(temp.data,end="<->")
    temp=temp.next
print("Tail")

#2.doublelinked list at end
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("Enter number of nodes:"))
for i in range(n):
    data=int(input("Enter the value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
print("DLL:")
temp=head
while temp:
    print(temp.data,end="<->")
    temp=temp.next
print("Tail")


#3.Doublelinkedlist delete at end:
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("Enter number of nodes:"))
for i in range(n):
    data=int(input("Enter the value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
print("DLL:")
temp=head
while temp:
    print(temp.data,end="<->")
    temp=temp.next
print("Tail")
#delete at the end
if head is None:
    print("DLL empty")
elif head.next is None:
    head=None
else:
    temp=head
    while temp.next:
        temp=temp.next
    temp.prev.next=None

print("DLL:after delete:")
temp=head
while temp:
    print(temp.data,end='<->')
    temp=temp.next
print("Tail")



#doubllinked list at begining:
class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("Enter number of nodes:"))
for i in range(n):
    data=int(input("Enter the value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
print("DLL:after delete")
temp=head
while temp:
    print(temp.data,end="<->")
    temp=temp.next
print("Tail")
##delete at the begining
if head is None:
    print("DLL empty")
else:
    head=head.prev.next
print("DLL:after delete:")
temp=head
while temp:
    print(temp.data,end='<->')
    temp=temp.next
print("Tail")'''


#deletion at end

class node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None
head=None
n=int(input("Enter number of nodes:"))
for i in range(n):
    data=int(input("Enter the value:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
        newnode.prev=temp
print("DLL:after delete")
temp=head
while temp:
    print(temp.data,end="<->")
    temp=temp.next
print("Tail")
#delete at the begining
if head is None:
    print("DLL empty")
else:
    head = head.next

    if head is not None:
        head.prev = None
print("DLL:after delete:")
temp=head
while temp:
    print(temp.data,end='<->')
    temp=temp.next
print("Tail")