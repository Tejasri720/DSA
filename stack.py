#push operation
'''stack=[]
n=int(input("enter no.of elements"))
for i in range(n):
    val=int(input("enter a value"))
    stack.append(val)
print("stack:",stack)'''

#peek operation
'''stack=[]
n=int(input("enter no.of elements"))
for i in range(n):
    val=int(input("enter a value"))
    stack.append(val)
print("stack:",stack)
print("peek:",stack[-1])'''

#pop operation
'''stack=[]
n=int(input("enter no.of elements"))
for i in range(n):
    val=int(input("enter a value"))
    stack.append(val)
print("stack:",stack)
if len(stack)==0:
    print("stack is empty!!!")
else:
    print("deleted elements",stack.pop())
print("stack:",stack)'''


#push operation delete all values till stack empty
'''stack=[]
n=int(input("enter number of elements:"))
for i in range(n):
    val=int(input("enter a value:"))
    stack.append(val)
print("stack",stack)
while len(stack)>0:
    print(stack.pop(),'delted')
print("Stack empty",stack)'''

#push operation till overflow
'''stack=[]
size=int(input("enter size"))
n=int(input("enter no.of elements:"))
for i in range(n):
    val=int(input("enter a value:"))
    if len(stack)==size:
        print('stack overflow')
    else:
        stack.append(val)
        print(val,'inserted')
print("stack:",stack)'''

#push operation and merge 2 stacks 1 3 5+2 4 =6 1 2 3 4 5 6
'''stack1=[]
stack2=[]
n=int(input("enter number of elements"))
for i in range(n):
    val=int(input("enter a value:"))
    stack1.append(val)
print("stack1",stack1)
for i in range(n):
    val=int(input("enter a value"))
    stack2.append(val)
print("stack2:",stack2)
stack1.extend(stack2)
stack1.sort()
print(stack1)'''

#merging two stacks with outnthe builtin
'''stack1=[]
stack2=[]
stack3=[]
n=int(input("enter number of elements"))
for i in range(n):
    val=int(input("enter a value:"))
    stack1.append(val)
print("stack1",stack1)
for i in range(n):
    val=int(input("enter a value"))
    stack2.append(val)
print("stack2:",stack2)
i,j=0,0
while i<len(stack1) and j<len(stack2):
    if stack1[i]<stack2[j]:
        stack3.append(stack1[i])
        i+=1
    else:
        stack3.append(stack2[j])
        j+=1
while i<len(stack1):
    stack3.append(stack1[i])
    i+=1
while j<len(stack2):
    stack3.append(stack2[j])
    j+=1
print("Merged Stack:",stack3)
 '''

#prefix in stack
'''exp=input("enter a expression:")
stack=[]
result=''
def priority(op):
    if op=='^':
        return 3
    elif op in '*/':
        return 2
    elif op in '+-':
        return 1
    return 0
exp=exp[::-1]
for ch in exp:
    if ch.isalnum():
        result+=ch
    else:
        while stack and priority(stack[-1])>=priority(ch):
            result+=stack.pop()
        stack.append(ch)
while stack:
    result+=stack.pop()
print("prifix:",result[::-1])'''

'''
#postfix
exp=input("enter a expression:")
stack=[]
result=''
def priority(op):
    if op=='^':
        return 3
    elif op in '*/':
        return 2
    elif op in '+-':
        return 1
    return 0

for ch in exp:
    if ch.isalnum():
        result+=ch
    else:
        while stack and priority(stack[-1])>=priority(ch):
            result+=stack.pop()
        stack.append(ch)
while stack:
    result+=stack.pop()
print("postfix:",result)'''

#prefic to postfix
'''exp=input("enter a expression:")
stack=[]
for ch in exp[::-1]:
    if ch.isalnum():
        stack.append(ch)
    else:
        a=stack.pop()
        b=stack.pop()
        stack.append(a+b+ch)
print("postfix",stack[-1])'''

#postfix to prefix
'''exp=input("Enter a expression:")
stack=[]
for ch in exp:
    if ch.isalnum():
        stack.append(ch)
    else:
        b=stack.pop()
        a=stack.pop()
        stack.append(ch+a+b)
print("postfix:",stack[-1])
'''

#browsing history
back = []
forward = []
history = []
current = ''

while True:
    print('\n1. Visit Website')
    print('2. Back')
    print('3. Forward')
    print('4. Display History')
    print('5. Exit')

    ch = int(input("Enter choice: "))

    if ch == 1:
        website = input("Enter website: ")

        if current != '':
            back.append(current)

        current = website
        history.append(website)
        forward.clear()

        print("Current website:", current)

    elif ch == 2:
        if back:
            forward.append(current)
            current = back.pop()
            print("Current website:", current)
        else:
            print("No previous website")

    elif ch == 3:
        if forward:
            back.append(current)
            current = forward.pop()
            print("Current website:", current)
        else:
            print("No forward website")

    elif ch == 4:
        print("\nBrowser History:")
        for site in history:
            print(site)

        print("\nCurrent Website:", current)

    elif ch == 5:
        print("Exiting Browser...")
        break

    else:
        print("Wrong choice")