DAY-4:

ERRORS:
syntax errors:violations of rules se by python errors.
logical errors:while writing code errors are thrown by compiler.
exceptions:try ,catch,throw,finally
except is also a keyword.
raise is used to throw an exception(similar to throw)
syn:
raise IndexBound:

print("starting line")
try:
    a=10/0
except:
    print("some exception is raised")
else:
    print("no exception raised the code works fine")
print("outside try block")
o/p:
exception:
starting line
some exception is raised
outside try block
no exception:
starting line
no exception raised the code works fine
outside try block
using finally:
print("starting line")
try:
    a=10/5
except:
    print("some exception is raised")
else:
    print("no exception raised the code works fine")
finally:
    print("this is a final block")
print("outside try block")
(finally executes irrespective of exception or no exception)
o/p:
starting line
no exception raised the code works fine
this is a final block
outside try block

print("starting line")
a=[11,12,33]
try:
    print(a[5])
except:
    print("index out of bound")
else:
    print("no exception raised the code works fine")
finally:
    print("this is a final block")
print("outside try block")
o/p:
starting line
index out of bound
this is a final block
outside try block

print("starting line")
a=[11,12,33]
try:
    print(y)
except:
    print("variable not defined")
else:
    print("no exception raised the code works fine")
finally:
    print("this is a final block")
print("outside try block")

o/p:
starting line
variable not defined
this is a final block
outside try block

print("starting line")

try:
    a=[11,12,33]
    print(a[5])
    a=10/0
    print(y)(#try block has only one exception at a time all three cannot be executed at once)
except ZeroDivisionError:
    print("division by zero")
except IndexError:
    print("index out of bound")
except NameError:
    print("variable not defined")
except:
    print("some exception was raised")
else:
    print("no exception raised the code works fine")
finally:
    print("this is a final block")
print("outside try block")
o/p:
starting line
variable not defined# index out of bound,division by zero at specified input in try block
this is a final block
outside try block


nested try block:
print("starting line")

try:
    
    a=[11,12,33]
    print(a[5])
    try:
        a=10/0
        print(y)
    except ZeroDivisionError:
        print("division by zero")
    finally:
        print("executed")
except IndexError:
    print("index out of bound")
except NameError:
    print("variable not defined")
else:
    print("no exception raised the code works fine")
finally:
    print("this is a final block")
print("outside try block")
o/p:
starting line
index out of bound
this is a final block
outside try block

print("starting line")

try:
    print("INNER TRY")
    try:
        a=10/0
        print(y)
        try:
            print(u)
        except IndexError:
            print("index out of bound")
        
        finally:
            print("executed")

    except ZeroDivisionError:
        print("division by zero")       
    
except NameError:
    print("variable not defined")
else:
    print("no exception raised the code works fine")
finally:
    print("this is a final block")
print("outside try block")
o/p:
starting line
INNER TRY
division by zero
no exception raised the code works fine
this is a final block
outside try block
notes:geeks for geeks,take you  forward

CONSTRUCTOR:
parameterized and default

encapsulation:wrapping of data members and member functions 
in a classi.e in a single unit is called encapsulation.

class Box:
    def __init__()(self,name,rn):
        self.name=name
        self.rn=rn
obj1=Box("zoya",34)
obj2=box("fathima",56)
print(obj1.name)

INHERITANCE:
Class BaseClass:
    {Body}
Class DerivedClass(BaseClass):
    {Body}
class Person(object):
   
  # Constructor
  def __init__(self, name, id):
    self.name = name
    self.id = id
 
  # To check if this person is an employee
  def Display(self):
    print(self.name, self.id)
 
 
# Driver code
emp = Person("Satyam", 102) # An Object of Person
emp.Display()

multilevel:
class Box:#parent
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
class student:
    def __init__(self,fees):
        self.fees=fees

class Box2(Box , student):#child
    def __init__(self,name,rollno,marks,fees):
        self.marks=marks
        student.__init__(self,fees)
        Box.__init__(self,name,rollno)
        #use self wn we invoke parent construtor using child
class Box3(Box2):
    def __init__(self,sem):
        self.sem=sem
        Box2.__init__(self,"shivaraj",12,23,20000)
#obj1=Box("zoya",34)
#print(obj1.name)
obj=Box3("2-1")
print(obj.sem)
print(obj.name)

obj2=Box2("shiv",12,13,2000)
print(obj2.fees)
print(obj2.marks)
print(obj2.name)
print(obj2.rollno)

obj3=Box2("raj",67,33,10000)
print(obj3.name)
print(obj3.rollno)
print(obj3.marks)
print(obj3.fees)

o/p:
2-1
shivaraj
2000
13
shiv
12
raj
67
33
10000

INTRODUCTION TO DDDDSSSSSSAAAAAAAAHHHHHH!!!!!!

linked list:
instead of null pointer we use none,and it has same head node and tail node which has
 data field and address field the last node is tail noden the 1st is head node.


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

obj1=Node(20)
#print(obj1.data)

obj2=Node(30)
obj3=Node(40)
obj4=Node(50)
obj1.next=obj2
obj2.next=obj3
obj3.next=obj4

curr=obj1
while curr!=None:
    print(curr.data,end="--> ")
    curr=curr.next
o/p:
20--> 30--> 40--> 50--> 





class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

obj1=Node(11)
#print(obj1.data)

obj2=Node(22)
obj3=Node(33)
obj4=Node(44)
obj5=Node(55)
obj6=Node(66)
obj7=Node(77)
obj8=Node(88)
obj9=Node(99)
obj10=Node(101)
obj1.next=obj2
obj2.next=obj3
obj3.next=obj4
obj4.next=obj5
obj5.next=obj6
obj6.next=obj7
obj7.next=obj8
obj8.next=obj9
obj9.next=obj10


curr=obj1
while curr!=None:
    print(curr.data,end="--> ")
    curr=curr.next
o/p:
11--> 22--> 33--> 44--> 55--> 66--> 77--> 88--> 99--> 101--> 




#insertion at head of node:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printll(head):
        curr=head
        while curr!=None:
            print(curr.data,end="--> ")
            curr=curr.next
        print()

def insertAtEndOfTail(head,ele):
        newBlock=Node(ele)

        if head==None:
            return newBlock

        curr=head
        while curr.next!=None:
            curr=curr.next
        curr.next=newBlock
        return head
l=[11,22,33,44,55,66,77,88,99,110]
head=None 
for ele in l:
    head=insertAtEndOfTail(head,ele) 

printll(head)   
o/p:
11--> 22--> 33--> 44--> 55--> 66--> 77--> 88--> 99--> 110--> 





class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def printll(head):
        curr=head
        while curr!=None:
            print(curr.data,end="--> ")
            curr=curr.next
        print(None)


#head   
#block creation for new value
#attaching the link
#change the head
def inserthead(head,ele):
    newblock=Node(ele)
    if head==None:
        return newblock
    newblock.next=head
    return newblock
l=[11,22,33,44,55,66,77,88,99,110]
head=None 
for ele in l:
    head=inserthead(head,ele) 

printll(head)   
o/p:
110--> 99--> 88--> 77--> 66--> 55--> 44--> 33--> 22--> 11--> None
advantage:dynamic memory allocation
dis:does not have indexing



specific pos:
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
 
def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next
    print()
 
def insertAtEndOfTail(head, ele):
    # Expectation is:
    # 1. It should create a new block with data as ele
    # 2. It should add this block at the end of insertAtEndOfTail
    # 3. Finally this function should return head of linked list
 
    # fulfilling expectation-1
    newBlock = Node(ele)
    # fulfilling expectation-2
    if head == None:
        return newBlock
    # 11 --> 22 --> 33 --> 44 --> 55 --> None
    curr = head 
    while curr.next != None:
        curr = curr.next 
    curr.next = newBlock
    # fulfilling expectation-3
    return head
 
 
# 11 --> 22 --> 33 --> 44 --> None
# head
 
# 1. Block creation for new value
# 2. Attaching link 
# 3. Change the head
 
def insertNodeAtHeadOfLinkedList(head, ele):
    # Expectation is:
    # 1. It should create a new block with data as ele
    # 2. It should add this block at the front of Linkedlist
    # 3. Finally this function should return head of linked list
    newBlock = Node(ele)
    if head == None:
        return newBlock
    newBlock.next = head 
    return newBlock
 
def insertAtSpecificPosition(head, position, value):
    newBlock = Node(value)
    if position == 1:
        newBlock.next = head 
        return newBlock
 
    index = 1 
    curr = head 
    while index != position - 1:
        curr = curr.next 
        index += 1 
 
    newBlock.next = curr.next
    curr.next = newBlock
    return head

(https://pastebin.com/tE6eVaTE got this code from here)
 
# 10 --> 22 --> 45 --> 67 --> 32 --> 78 --> None
# 1      2       3     4      5      6 
 
# 67 -> 790 --> 32 --> 78 --> None
 
# (1, 790)
# (position = 5)
 
 
# 2500
# (1876, 23)
# (position, value)
# head to (position - 1)
 
 
 
# head, position, value
 
# 1. creating newBlock for given value
# 2. 
# 10 --> 22 --> 45 --> 67 --> 790 ---> 32 --> 78 --> None
# 1      2       3     4      5      6       
 
l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None 
for ele in l:
    # head = insertAtEndOfTail(head, ele)
    head = insertNodeAtHeadOfLinkedList(head, ele)
 
printLinkedList(head)
head = insertAtSpecificPosition(head, 1, 1009)
printLinkedList(head)
o/p:
110 --> 99 --> 88 --> 77 --> 66 --> 55 --> 44 --> 33 --> 22 --> 11 --> 
1009 --> 110 --> 99 --> 88 --> 77 --> 66 --> 55 --> 44 --> 33 --> 22 --> 11 --> 



DAY-5:
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
 
def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next
    print(None)

def inserthead(head,ele):
    newblock=Node(ele)
    newblock.next=head
    return newblock
 
def deletetail(head):
    
    curr = head 
    previous=None
    previous=curr
    while curr.next!=None:
        previous=curr
        curr=curr.next
    previous.next=None
    return head
 
 

    
l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None 
for ele in l:
     head = inserthead(head, ele)
printLinkedList(head)
head = deletetail(head)
printLinkedList(head)
head = deletetail(head)
printLinkedList(head)


o/p:
110 --> 99 --> 88 --> 77 --> 66 --> 55 --> 44 --> 33 --> 22 --> 11 --> None
110 --> 99 --> 88 --> 77 --> 66 --> 55 --> 44 --> 33 --> 22 --> None
110 --> 99 --> 88 --> 77 --> 66 --> 55 --> 44 --> 33 --> None
https://pastebin.com/1FeCaphn


delete head:

def deleteHeadNode(head):
	if  head==None:
	return None
	secondNode=head.next
head.next=None
return secondNode

deleting at specific position:
def deleteAtSpecific(head,position):
	curr=head
	index=1
	while index!=position-1:
		curr=curr.next
		index=index+1
	mainNode=curr.next
	nextNode=mainNode.next
	mainNode.next=None
	curr.next=None
	curr.next=nextNode

class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
 
def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next
    print(None)

def inserthead(head,ele):
    newblock=Node(ele)
    newblock.next=head
    return newblock
 
def deleteAtSpecific(head,position):
    
    if position == 1:
        return deleteAtSpecific(head)
    curr = head 
    index=1
    
	while index!=position-1:
		curr=curr.next
		index=index+1
	mainNode=curr.next
	nextNode=mainNode.next
	mainNode.next=None
	curr.next=None
	curr.next=nextNode

l = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
head = None 
for ele in l:
     head = inserthead(head, ele)
printLinkedList(head)
head = deleteAtSpecific(head,4)
printLinkedList(head)
head = deleteAtSpecific(head,2)
printLinkedList(head)

https://pastebin.com/nbNduSC1
https://pastebin.com/xtKGpArE

#DOUBLY LINKED LIST
class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev=None

def ltr(head):
    print("left to right")
    curr = head
    while curr != None:
        print(curr.data, end = " --> ")
        curr = curr.next
    print(None)

def rtl(tail):
    print("right to left")
    curr=tail
    while curr!=None:
        print(curr.data,end="-->")
        curr=curr.prev
    print(None)



obj1=Node(121)
obj2=Node(145)
obj3=Node(678)
obj4=Node(89)
obj5=Node(12)
obj1.next=obj2
obj2.prev=obj1

obj2.next=obj3
obj3.prev=obj2

obj3.next=obj4
obj4.prev=obj3

obj4.next=obj5
obj5.prev=obj4
 
ltr(obj1)
rtl(obj5)

O/P:
left to right
121 --> 145 --> 678 --> 89 --> 12 --> None
right to left
12-->89-->678-->145-->121-->None


 











