#Queues
#insertion of elements using queue
'''from queue import Queue
q=Queue()
n=int(input("Enter no of elements:"))
for i in range(n):
    val=int(input("Enter value:"))
    q.put(val)
print("Queue elements :")
for i in range(q.qsize()):
    val=q.get()
    print(val,end=' ')
    q.put(val)'''

#delete of elements using queue and display empty
'''from queue import Queue
q=Queue()
n=int(input("Enter no of elements:"))
for i in range(n):
    val=int(input("Enter value:"))
    q.put(val)
while not q.empty():
    print(q.get(), ":deleted")
print("Queue empty")'''

#insert elements in a fixed queue
'''from queue import Queue
q=Queue(3)
n=int(input("Enter no of elements:"))
for i in range(n):
    val=int(input("Enter value:"))
    if not q.full():
        q.put(val)
    else:
        print("Queue is full")
if q.full():
    print("Queue is full")
print("Queue:", list(q.queue))'''


#collection in queues
#*Counter
'''from collections import Counter
nums=input("enter numbers:").split()
c=Counter(nums)
print("counter:",c)
print("Most common,c.most_common(1))'''


'''from collections import defaultdict
d=defaultdict(int)
n=int(input("enter a value:"))
for i in range(n):
    val=input("enter value")
    d[val]+=1
print("Dictionary:",dict(d))'''

'''#orderedDict
from collections import OrderedDict
d=OrderedDict()
n=int(input("enter a value"))
for i in range(n):
    key=input("Enter key:")
    val=input("enter a value")
    d[key]=val
print("ordered dictionary:",d)
'''

#named tuple
'''
from collections import namedtuple
student=namedtuple("student",["name","age","marks"])
name=input("enter name")
age=int(input("enter age"))
marks=int(input("enter marks"))
s=student(name,age,marks)
print("student:",s)
print("Marks:",s.marks)
print("Age:",s.age)'''


'''
#ChainMap
from collections import ChainMap

d1 = {}
d2 = {}

n = int(input("Enter number of elements in d1: "))
for i in range(n):
    key = input("Enter key: ")
    val = input("Enter value: ")
    d1[key] = val

n = int(input("Enter number of elements in d2: "))
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d2[key] = value

c = ChainMap(d1, d2)

print("1st dictionary:", d1)
print("2nd dictionary:", d2)
print("ChainMap:", c)'''



'''from collections import UserDict,UserList
class MyDict(UserDict):
    def add_data(self,key,value):
        self.data[key]=value
d=MyDict()
n=int(input("enter a number"))
for i in range(n):
    key=input("enter key")
    value=input("enter a value")
    d.add_data(key,value)
print("dictionary:",d)
    '''

'''from collections import UserDict, UserList

class MyList(UserList):
    def add_element(self, value):
        self.data.append(value)

l = MyList()

numbers = input("Enter numbers: ").split()

for i in numbers:
    l.add_element(i)

print("List:", l)'''