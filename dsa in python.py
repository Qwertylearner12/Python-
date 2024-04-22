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
#DELETING AT SPECIFIC POSITION IN SLL:
class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
 
def insertAtEndOfTail(head, ele):
    newBlock = Node(ele)
    if head == None:
        return newBlock
    curr = head 
    while curr.next != None:
        curr = curr.next 
    curr.next = newBlock
    return head
 
def printlist(head):
    # below line of code is assigning head to curr variable
    curr=head
 
    # below line is checking whether curr reached none or not
    while curr!=None:
 
        # here we are trying to print data in curr pointer 
        print(curr.data,end=" ")
        curr=curr.next
    print()
 
 
# 1. Deleting head node in a linked list
# 2. Deleting node at specific position in linked list
 
# Before deletion
# 21 --> 45 --> 100 --> 12 --> 78 --> 56 --> None 
# 1       2      3       4      5      6 
 
# position = 4
 
# 9500 
# 5631 
 
def deleteHeadNodeInLinkedList(head):
    # delete link between first and second node
    # change the head to newHead
    if head == None:
        return None 
 
    secondNode = head.next 
    head.next = None 
    return secondNode
 
# After deletion
# 21 --> 45 --> 100 --> 78 --> 56 --> None 
# 1       2      3       4      5       
 
 
def deleteNodeAtSpecificPosition(head, position):
    if position == 1:
        return deleteHeadNodeInLinkedList(head)
    curr = head 
    index = 1 
    while index != position - 1:
        curr = curr.next 
        index += 1 
    # curr --> points to (position - 1)
    mainNode = curr.next 
    # mainNode --> points to (position)
    nextNode = mainNode.next 
    # nextNode --> points to (position + 1)
    # 5630 --> None 
    # 5631 --> None 
    # 5632
    # 5630 --> 5632
    mainNode.next = None 
    curr.next = None 
    curr.next = nextNode 
    return head
 
# 21 --> None 
# 45 --> 100 --> 12 
 
n=int(input())
l=list(map(int,input().split()))
head=None
for ele in l:
    head=insertAtEndOfTail(head,ele)
printlist(head)
head = deleteHeadNodeInLinkedList(head)
printlist(head)
 
head = deleteHeadNodeInLinkedList(head)
printlist(head)

#insert at tail node
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
    tail=head
    while tail.next!=None:
        tail=tail.next
    curr=tail
    while curr!=None:
        print(curr.data,end="-->")
        curr=curr.prev
    print(None)

def addTail(head,val):
    newblock=Node(val)
    if head==None:
        return newblock
    tail=head
    while tail.next!=None:
        tail=tail.next
    tail.next=newblock
    newblock.prev=tail
    return head

l=[11,22,33,44,55,66,77]
head=None
for ele in l:
    head=addTail(head,ele)
ltr(head)
rtl(head)

o/p:
left to right
11 --> 22 --> 33 --> 44 --> 55 --> 66 --> 77 --> None
right to left
77-->66-->55-->44-->33-->22-->11-->None
#insert at head:
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
    tail=head
    while tail.next!=None:
        tail=tail.next
    curr=tail
    while curr!=None:
        print(curr.data,end="-->")
        curr=curr.prev
    print(None)


def addHead(head,val):
    newblock=Node(val)
    if head==None:
        return newblock
    newblock.next=head
    head.prev=newblock
    return newblock

l=[11,22,33,44,55,66,77]
head=None
for ele in l:
    head=addHead(head,ele)
ltr(head)
rtl(head)

o/p:
left to right
77 --> 66 --> 55 --> 44 --> 33 --> 22 --> 11 --> None
right to left
11-->22-->33-->44-->55-->66-->77-->None
https://pastebin.com/EdnnK3GV
https://pastebin.com/9wYRny3g

#POLYMORPHISM:
class b1:
    def __init__(self,name):
        self.name=name

    def printde(self):
        print("printing name:",self.name)

class b2(b1):
    def __init__(self,name,roll):
        self.roll=roll
        b1.__init__(self,name)
    def printde(self):
        print("printing rollno:",self.roll)

obj=b2("raj",32)
obj.printde()
O/P:
printing rollno: 32

 











