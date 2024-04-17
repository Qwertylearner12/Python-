DAY-3:
keys can be strings n also integer .it allows to store multiple data indexes.
dictionaries are new data strucures used to store organized data efficiently.
dict()it creates an empty dictionary.(without any parameters).
both lowercase and uppercase can be inserted in the same dictionary n also integers can be accepted.

word=input()
print(word)
store=dict()
print(store)
store['d']=23
#here d is the key and 23 is the value
store['Q']=12
store[12]=11
store["hello"]=222
print(store)
o/p:
dictionaries
{}
{'d': 23, 'Q': 12, 12: 11, 'hello': 222}
dictionary name using .keys  with name of the dictionary shows all keys in dictionary.

word=input()
print(word)
store=dict()
print(store)
store['d']=23
#here d is the key and 23 is the value
store['Q']=12
store[12]=11
store["hello"]=222
print(store)
allkeys=store.keys()
print(allkeys)
#for-each loop:
for ele in allkeys:
        print(ele)
for ch in "adcdef":
    print(ch)
for val in[12,13,14,1,2,3,2]:
        print(val)
o/p:
dictionaries
{}
{'d': 23, 'Q': 12, 12: 11, 'hello': 222}
dict_keys(['d', 'Q', 12, 'hello'])
d
Q
12
hello
a
d
c
d
e
f
12
13
14
1
2
3
2

word=input()
print(word)
store=dict()

for ch in word:
    if ch in store:
        store[ch]+=1
    else:
        store[ch]=1
print(store)
#resultchar=r,result frequency=f
r='#'
f=0

allkeys=store.keys()
for ele in allkeys:
    if store[ele]>f:
        f=store[ele]
        r=ele
print(r,f)
o/p:
abcdefghijachhfdyghskdloigfdz
{'a': 2, 'b': 1, 'c': 2, 'd': 4, 'e': 1, 'f': 3, 'g': 3, 'h': 4, 'i': 2, 'j': 1, 'y': 1, 's': 1, 'k': 1, 'l': 1, 'o': 1, 'z': 1}
d 4








* 
# # 
* * * 
# # # # 
n=int(input())
for i in range(n):
    for j in range(i+1):
        if i%2==0:
         print("*",end=" ")
        else:
         print("#",end=" ")
    print()

for i in range(n):
    for j in range(n-i-1):
        print(' ', end=' ')
    for k in range(2*i+1):
        print('*', end=' ')
    print()(for equilateral triangle)


class card:
    def __init__(self,image,price,rating,des,deli,com,brand):
        self.image=image
        self.cost=price
        self.a=rating
        self.b=des
        self.c=deli
        self.d=com
        self.e=brand
s1=card("zoya",93,"good","cute","grace",2,3)
print(s1.image)
print(s1.cost)
print(s1.b)

s2=card("fathima",45,"good","cute","grace",32,2)
print(s2.image)
print(s2.cost)

s3=card("z",81,98,"good","cute","grace",98)
print(s3.image)
print(s3.cost)
print(s3.a)


s4=card("zo","good","cute","grace",90,98,98)
print(s4.image)
print(s4.cost)
print(s4.d)


s5=card("zoy",3,"good","cute","grace",98,90)
print(s5.image)
print(s5.cost)
print(s5.c)

o/p:
zoya
93
cute
fathima
45
z
81
98
zo
good
98
zoy
3
grace

amazon themes:
class card:
    def __init__(self,image,price,rating,des,deli,com,brand):
        self.image=image
        self.price=price
        self.rating=rating
        self.des=des
        self.deli=deli
        self.com=com
        self.brand=brand
    def p(self):
        print("product brand is:",self.brand)
        print("product cost is:",self.price)       
        print("product rating is:",self.rating)

comforlaptop=["this is good","okay","not good"]
laptop=card("url-1",90000,4.5,"this is a good performer","4days",comforlaptop,"samsung")
laptop.p()
#print(laptop.image)
#print(laptop.price)
comformobile=["not working","okay","not good"]
mobile=card("url-2",9000,3.5,"this is a good performer","4days",comformobile,"vivo")
mobile.p()
comforwatch=["this is gross","okay","poor"]
watch=card("url-3",90000,4.5,"this is a good performer","4days",comforwatch,"trendxlsv")
watch.p()

o/p:
product brand is: samsung
product cost is: 90000
product rating is: 4.5
product brand is: vivo
product cost is: 9000
product rating is: 3.5
product brand is: trendxlsv
product cost is: 90000
product rating is: 4.5






class card:
    def __init__(self,image,price,rating,des,deli,com,brand):
        self.image=image
        self.price=price
        self.rating=rating
        self.des=des
        self.deli=deli
        self.com=com
        self.brand=brand
    def p(self):
        print("product brand is:",self.brand)
        print("product cost is:",self.price)       
        print("product rating is:",self.rating)

    def q(self):
        print("calculating gst")
    
    def r(self,extraprice):
        print("printing invoice")


        def z(self,cost):
            print("m1 invoked")
    
    def zo(self,bearing,amount,grades):
        print("m2 incoked")

o1=card(1,2,3,4,5,6,7)
o1.r(1200)
o1.q()

    
ob1=card()
o1.z1(12,13)
o1.z2(13,15,16,17)


comforlaptop=["this is good","okay","not good"]
laptop=card("url-1",90000,4.5,"this is a good performer","4days",comforlaptop,"samsung")
laptop.p()
#print(laptop.image)
#print(laptop.price)
comformobile=["not working","okay","not good"]
mobile=card("url-2",9000,3.5,"this is a good performer","4days",comformobile,"vivo")
mobile.p()
comforwatch=["this is gross","okay","poor"]
watch=card("url-3",90000,4.5,"this is a good performer","4days",comforwatch,"trendxlsv")
watch.p()
[try to complte the code of 1 member function calling 1 object n 2 obj calling 1 mf]





n=int(input())
for i in range(n):
    for j in range(i+1):
        if i==0:
            print("*",end=" ")
        elif i>0:
            print("#",end=" ")
        else:
            print("$",end=" ")
    print()
* 
# # 
# # # 
# # # # 
n=int(input())
space=n-1
stars=1
for i in range(n):
    for j in range(space):
        print("-",end=" ")
    for j in range(stars):
        print("*",end=" ")
    print()
    space=space-1
    stars=stars+1
- - * 
- * * 
* * * 
def solveIt2():
    print("i am solveit2")
def solve4():
    print("i am solve 4")
    print("this is getting executed")
    solveIt2()

def Solve():
    print("this is line 111")
    print("this is line 112")
    solve4()

def Sum(n1,n2):
    Solve()
    result=n1+n2
    return result



n1=int(input())
n2=int (input())
result=Sum(n1,n2)
print(result)

o/p:
this is line 111
this is line 112
i am solve 4
this is getting executed
i am solveit2
50
print("hello")
def solveIt2():
    print("1st is executed")
    print("i am solveit2")

    print("i am not getting printed")
def solve4():
    print("i am solve 4")
    print("this is getting executed")
    solveIt2()
    print("2nd is getting executed")

def Solve():
    print("this is line 111")
    print("this is line 112")
    solve4()
    print("solve 4 has still executions")

def Sum(n1,n2):
    print("after  execution")
    Solve()
    print("ntg printed")
    result=n1+n2
    print("before execution")
    return(result)

    print("lasr line  is getting executed")

n1=int(input())
n2=int (input())
result=Sum(n1,n2)
print(result)
o/p:
hello
after  execution
this is line 111
this is line 112
i am solve 4
this is getting executed
1st is executed
i am solveit2
i am not getting printed
2nd is getting executed
solve 4 has still executions
ntg printed
before execution
50
lists:
a=[1,2,"a","z",4,5]
n=len(a)
key=4
for i in range(n):
    if(a[i]==key):
        print("found",i)
    else:
        print("not found",)
o/p:
not found
not found
not found
not found
found 4
not found
a=[1,2,"a","z",4,5]
n=len(a)
key=4
for i in range(n):
    if(a[i]==key):
        print("found",i)
        break;
o/p:
found 4
a=[1,2,"a","z",4,5]
n=len(a)
key=5
v=0
for i in range(n):
    if a[i]==key:
        print("found",i)
        break;

    if(v==0):
        print("not found"){"linear search"}
tranversing number of times an element is specified in a list:
a=[1,2,"a","z",3,2,1]
n=len(a)
key=2
for i in range(n):
    if a[i]==key:
        print(a[i])
        n=n+1
    o/p:
2
2
tranversal=2
def t(l,r):
    res=0
    n=len(l)
    for i in range(n):
        if l[i]==k:
            res=res+1
    return res
    

l=[1,2,3,4,3,2,2,1,2]
k=2
r=t(l,k)


print("occurance:",r)
o/p:
occurance:4
def t(l,r):
    res=0
    n=len(l)
    for i in range(n):
        if l[i]==k:
            res=res+1
    return res
    

l=[1,2,3,4,3,2,2,1,2]
k=2
res=t(l,k)


print("occurance:",r)
l2=[1,4,5,6,6,7,6,8]
k2=6
res=t(l2,k2)
print(res){check code}
def t(l,r):
    res=0
    n=len(l)
    for i in range(n):
        if l[i]>k:
            res=res+1
    return res
    

l=[1,2,3,4,3,2,2,1,2]
k=2
res=t(l,k)


print("occurance:",res)
o/p:occurance: 3

def e(l):
    res=0
    n=len(l)
    for i in range(n):
         if l[i]%2==0:
            res=res+1
    return res
        
l=[1,2,3,4,3,2,2,1,2,6]
res= e(l)
print("even number are",res)
l=[1,2,3,4,3,2,2,1,2,6]
l.sort()
print("largest=",l[-1]){with built in function}
def t(l):
    large=l[0]
    for i in l:
        if i>large:
            large=i
    return large
    

l=[1,2,3,4,3,2,2,1,2]
print("largest in")
print(t(l))
def m(l):
    res=0
    n=len(l)
    for i in range(n):
        if l[i]>res:
            res=l[i]
    return res
#smallest number:

l=[1,2,3,4,5,78,9,5,3]
res=m(l)
print(res)
def m(l):
    res=0
    n=len(l)
    for i in range(n):
        if l[i]>res:
            res=l[i]
    return res

l=[1,2,3,4,5,78,9,5,3]
res=m(l)
print(res)

n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print("* ",end=" ")
    print()



for i in range(n-1):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i-1):
        print("* ",end=" ")
    print()
o/p:
      *  
    *  *  
  *  *  *  
*  *  *  *  
  *  *  *  
    *  *  
      *  
dynamic ALLOCATION OF LISTS:
l=list(map(int,input().split()))
print(l)

print(l[-1])
print(l[-2])
l=list(map(int,input().split()))
print(l)

print(l[-1])
print(l[-2])
res=max(l)
print(res)
res=min(l)
print(res)
o/p:
4, 5, 6, 7, 3, 3, 22, 4, 5, 6]
6
5
22
3
note:set has no indexing ,conversion can be done from set to list.

l=list(map(int,input().split()))
print(l)
v=set(l)
print(v)
w=list(set(v))
print(w){i/p drawn from set in w}
o/p:
[4, 5, 6, 7, 3, 3, 22, 4, 5, 6]
{3, 4, 5, 6, 7, 22}
[3, 4, 5, 6, 7, 22]
l=list(map(int,input().split()))
print(l)
w=list(set(l))
print(w)
o/p:
[4, 5, 6, 7, 3, 3, 22, 4, 5, 6]
[3, 4, 5, 6, 7, 22]
word=input()
print(word[5])o/p:(compiler)1

word=input()
word[1]='r'
print(word)
note:strings are immutable cant be cahnged in python 
but we can use slicing to do so

word=input()
#slicing
#T=WORD[LEFTVALUE:RIGHTVALUE]
t=word[2:5]
print(t)
if only[2:] is given it starts from index two ande ends at the last word
 if[:]ntg is given then full word is printed here we say complier
for the below code -ve indexing can be done :
word[leftvalue :right value:-1] the string is reversed


word=input()
t=word[5:10]
print(t)
t=word[14:21]
print(t)
t=word[21:26]
print(t)
t=word[27:]
print(t)
t=word[0:4]
print(t)
t=word[5:16]
print(t)
t=word[17:]
print(t)
t=word[9:14]
print(t)
t=word[14:20]
print(t[::-1])
t=(word[5:13])
print(t[::-1])
o/p:
learn
python 
laung
age
i am
learning py
hon launguage
ning 
nohtyp
gninrael

word=input()
t=word[5:10]
print(t)
t=word[14:21]
print(t)
t=word[21:26]
print(t)
t=word[27:]
print(t)
t=word[0:4]
print(t)
t=word[5:16]
print(t)
t=word[17:]
print(t)
t=word[9:14]
print(t)
t=word[14:20]
print(t[::-1])
t=(word[5:13])
print(t[::-1])
t=word[0:4]
print(t[::-1])
t=word[16:26]
print(t[::-1])
t=word[2:10]
print(t[::-1])
t=word[16:23]
print(t[::-1])
o/p:

learn
python 
laung
age
i am
learning py
hon launguage
ning 
nohtyp
gninrael
ma i
gnual noht
nrael ma
al noht

DAY-3:
keys can be strings n also integer .it allows to store multiple data indexes.
dictionaries are new data strucures used to store organized data efficiently.
dict()it creates an empty dictionary.(without any parameters).
both lowercase and uppercase can be inserted in the same dictionary n also integers can be accepted.

word=input()
print(word)
store=dict()
print(store)
store['d']=23
#here d is the key and 23 is the value
store['Q']=12
store[12]=11
store["hello"]=222
print(store)
o/p:
dictionaries
{}
{'d': 23, 'Q': 12, 12: 11, 'hello': 222}
dictionary name using .keys  with name of the dictionary shows all keys in dictionary.

word=input()
print(word)
store=dict()
print(store)
store['d']=23
#here d is the key and 23 is the value
store['Q']=12
store[12]=11
store["hello"]=222
print(store)
allkeys=store.keys()
print(allkeys)
#for-each loop:
for ele in allkeys:
        print(ele)
for ch in "adcdef":
    print(ch)
for val in[12,13,14,1,2,3,2]:
        print(val)
o/p:
dictionaries
{}
{'d': 23, 'Q': 12, 12: 11, 'hello': 222}
dict_keys(['d', 'Q', 12, 'hello'])
d
Q
12
hello
a
d
c
d
e
f
12
13
14
1
2
3
2

word=input()
print(word)
store=dict()

for ch in word:
    if ch in store:
        store[ch]+=1
    else:
        store[ch]=1
print(store)
#resultchar=r,result frequency=f
r='#'
f=0

allkeys=store.keys()
for ele in allkeys:
    if store[ele]>f:
        f=store[ele]
        r=ele
print(r,f)
o/p:
abcdefghijachhfdyghskdloigfdz
{'a': 2, 'b': 1, 'c': 2, 'd': 4, 'e': 1, 'f': 3, 'g': 3, 'h': 4, 'i': 2, 'j': 1, 'y': 1, 's': 1, 'k': 1, 'l': 1, 'o': 1, 'z': 1}
d 4

while loop:
n=int(input())
i=56
while i<=n:
    print(i)
    i+=1
o/p:
56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78
 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 (prints in one line use end n i/p:=97)

n=int(input())
i=1222
while i>=n:
    print(i,end=' ')
    i-=1
o/p:1222to 995

n=int(input())
i=1
while i<=n:
    print(n*i)

n=int(input())
multiplier = 5
counter = 1
  
while counter <= 10: 
    result = counter * multiplier 
    print(f"{counter} x {multiplier} = {result}") 
    counter += 1

    i+=1
o/p:
1 x 5 = 5
2 x 5 = 10
3 x 5 = 15
4 x 5 = 20
5 x 5 = 25
6 x 5 = 30
7 x 5 = 35
8 x 5 = 40
9 x 5 = 45
10 x 5 = 50
print even numbers from 12 to 56:
n=int(input())
i=12
while i<=56:
    if i%2==0:
        print(i)
        i=i+2
    else:
        print("invalid")


value=70
while value>=7:
    print(value)
    value-=7

i=12
while i<=56:
    if i%2==0:
        print(i)
        i=i+2

constructor in python is named as init__()
defining a constructor:
def__init__():
it has a keyword self in python.
object n calss in python:
class Box:
    def __init__(self,currname,currrn,curra,currb,currc,currd,curre):
        self.name=currname
        self.rn=currrn
        self.a=curra
        self.b=currb
        self.c=currc
        self.d=currd
        self.e=curre
s1=Box("zoya",93,98,90,90,98,98)
print(s1.name)
print(s1.rn)
print(s1.d)

s2=Box("fathima",45,67,8,93,32,2)
print(s2.name)
print(s2.rn)
o/p:
zoya
93
98
fathima
45

class Box:
    def __init__(self,currname,currrn,curra,currb,currc,currd,curre):
        self.name=currname
        self.rn=currrn
        self.a=curra
        self.b=currb
        self.c=currc
        self.d=currd
        self.e=curre
s1=Box("zoya",93,98,90,90,98,98)
print(s1.name)
print(s1.rn)
print(s1.d)

s2=Box("fathima",45,67,8,93,32,2)
print(s2.name)
print(s2.rn)

s3=Box("z",81,98,90,90,98,98)
print(s3.name)
print(s3.rn)
print(s3.d)


s4=Box("zo",93,8,90,90,98,98)
print(s4.name)
print(s4.rn)
print(s4.d)


s5=Box("zoy",3,98,0,90,8,98)
print(s5.name)
print(s5.rn)
print(s5.d)

o/p:
zoya
93
98
fathima
45
z
81
98
zo
93
98
zoy
3
8

pin=2387
count=3
for i in range(3):
    curr=int(input())
    
    if curr==pin:
        print("logged in")
        break
    else:
        if(count==1):
            print(" BLOCKED try after 24 hrs")
        else:
            print("incorrect password,you are left with",count-1,"to login")
    count-=1






