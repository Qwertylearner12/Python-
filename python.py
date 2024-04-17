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





