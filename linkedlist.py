#sll insert from begining
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input('Enter number of nodes:'))
for i in range(n):
    data=int(input("enter values:"))
    newnode=node(data)
    newnode.next=head
    head=newnode
print("SLL")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print('tail')



#sll insert  from end
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input('Enter number of nodes:'))
for i in range(n):
    data=int(input("enter values:"))
    newnode=node(data)
    if head is  None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
print("SLL")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print('tail')'''






#insert at end delete at begining
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter number of nodes:"))
for i in range(n):
    data=int(input("enter vale:"))
    newnode=node(data)
    if head is None:
        head=newnode
    else:
        temp=head
        while temp.next:
            temp=temp.next
        temp.next=newnode
print("SLL:before delete:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print('tail')
#delete at begining
if head is None:
    print("SLL empty.....")
else:
    head=head.next
print("SLL:after delete:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print('tail')
'''


#insert from begining and delete at end 
'''class node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=None
n=int(input("enter number of nodes:"))
for i in range(n):
    data=int(input("enter vale:"))
    newnode=node(data)
    newnode.next=head
    head=newnode
print("SLL:before delete:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print('tail')
#delete at end
if head is None:
    print("SLL empty....")
elif head.next is None:
    head=None
else:
    temp=head
    while temp.next.next:
        temp=temp.next
    temp.next=None
print("SLL:after delete:")
temp=head
while temp:
    print(temp.data,end='->')
    temp=temp.next
print('tail')'''


#insert at position 
'''class node:
    def __init__(self,data):
        self.data= data
        self.next= None 
head = None 
n = int(input("Enter number of nodes : "))
for i in range(n):
    data = int(input("Enter a value : "))
    newnode = node(data)
    newnode.next = head
    head= newnode
print("SLL: before insert: ")
temp= head 
while temp:
    print(temp.data, end= '->')
    temp= temp.next 
print("Tail")
pos= int(input("Enter the position :"))
data = int(input("enter the data "))
newnode= node(data)
if pos==1 :
    newnode.next= head 
    head= newnode 
else:
    temp= head 
    count= 1 
    while temp and count <pos-1 :
        temp= temp.next 
        count+=1 
    if temp is None :
        print("Invalid position")
    else:
        newnode.next= temp.next 
        temp.next = newnode 
print("SLL: after insert: ")
temp= head 
while temp:
    print(temp.data, end= '->')
    temp= temp.next 
print("Tail")'''

#delete a value in a sll by position
'''class node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

# Insertion at end
n = int(input("Enter no.of nodes: "))

for i in range(n):
    data = int(input("Enter value: "))
    newnode = node(data)

    if head is None:
        head = newnode
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = newnode

print("After insertion:")
temp = head

while temp:
    print(temp.data, end='->')
    temp = temp.next

print("tail")

# Deletion at specific position
pos = int(input("Enter the position: "))

if pos < 1 or head is None:
    print("Invalid position")

elif pos == 1:
    head = head.next

else:
    temp = head
    count = 1

    while temp.next and count < pos - 1:
        temp = temp.next
        count += 1

    if temp.next is None:
        print("Invalid position")
    else:
        temp.next = temp.next.next

print("After deletion:")
temp = head

while temp:
    print(temp.data, end='->')
    temp = temp.next

print("tail")'''

# same but here we give the value that to delete in the placem f position
'''
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

# Insertion at end
n = int(input("Enter no.of nodes: "))

for i in range(n):
    data = int(input("Enter value: "))
    newnode = node(data)

    if head is None:
        head = newnode
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = newnode

print("After insertion:")
temp = head

while temp:
    print(temp.data, end='->')
    temp = temp.next

print("tail")

# Deletion at specific position
value = int(input("Enter the Value: "))

if head is None:
    print("SLL is empty")

elif head.data == value:
    head = head.next

else:
    temp = head

    while temp.next and temp.next.data!=value:
        temp = temp.next

    if temp.next is None:
        print("value not found")
    else:
        temp.next = temp.next.next

print("After deletion:")
temp = head

while temp:
    print(temp.data, end='->')
    temp = temp.next

print("tail")


#reversed singlr linked list
class node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = None

# Insertion at end
n = int(input("Enter no.of nodes: "))

for i in range(n):
    data = int(input("Enter value: "))
    newnode = node(data)

    if head is None:
        head = newnode
    else:
        temp = head
        while temp.next:
            temp = temp.next
        temp.next = newnode

print("After insertion:")
temp = head

while temp:
    print(temp.data, end='->')
    temp = temp.next

print("tail")

prev =None
current=head
while current:
    nextnode=current.next
    current.next=prev
    prev= current
    current=nextnode
head=prev

print("reversed sll")
temp = head
while temp:
    print(temp.data, end='->')
    temp = temp.next

print("tail")

'''