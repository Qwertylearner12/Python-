DAY--7:

SEARCHING AND SORTING:
THE TIME COMPLEXITY OF LINEAR SEARCH IS 0(N)
N=0(N)
order of N,where N is the length f the list.
#BINARY SEARCH:
nums=[12,34,2,56,90,33,89,120,20]
nums=sorted(nums)
target=120
left=0
right=len(nums)-1
found=False

while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        found=True
        break
    elif nums[mid]>target:
        right=mid-1
    else:
        left=mid+1
if found==True:
    print("target found")
else:
    print("not found")

O/P:
target found
#INPUT FROM USER :
nums=map(int,input().split())
nums=sorted(nums)
target=int(input())
left=0
right=len(nums)-1
found=False

while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        found=True
        break
    elif nums[mid]>target:
        right=mid-1
    else:
        left=mid+1
if found==True:
    print("target found")
else:
    print("not found")

#TIME COMPLEXITY ORDER(IN TIME AS WELL AS SPACE):
0(1)<0(log N)<0(sqrt N)<0(N)<0(N log N)<0(N*N)<0(N*N*N)<....
https://pastebin.com/i5AYjhCP
sorting:
bubble sort
selection sort
insertion sort
merge sort
quick sort
#bubble sort:
arrays=[2,12,34,21,37,45]
for 1st iteration:		
it compares two elements of the arrays.
compare 2<12
there is no replacement
now the  array compares 12<34
it is true and the array does not changes
now it compares 34<21 the condition is false now the new array is 
array=[2,12,21,34,37,45]
now compare 34<37 true
then compare 37<45 true 
hence the array is sorted using bubble sort.
the array after the final iteration is :
array=[2,12,21,34,37,45]
#code:
arr=[21,34,56,24,2,38]
length=len(arr)
print("before sorting")
print(arr)
for i in range(length):
    for j in range(0,length-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("sorted array:")
for i in range(length):
    print(arr[i],end=" ")
o/p:
before sorting
[21, 34, 56, 24, 2, 38]
sorted array:
2 21 24 34 38 56 
https://pastebin.com/FwD6uqAw

def bs(arr):
    length=len(arr)
    for i in range(length-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        print(arr)
arr=[12,2,34,20,56,43,45,100,89,50]
print("before sorting")
print(arr)
print("sorted array:")
bs(arr)
print(arr)
print("after sorting")
print(arr)
o/p:
before sorting
[12, 2, 34, 20, 56, 43, 45, 100, 89, 50]
sorted array:
[2, 12, 20, 34, 43, 45, 56, 89, 50, 100]
[2, 12, 20, 34, 43, 45, 56, 50, 89, 100]
[2, 12, 20, 34, 43, 45, 50, 56, 89, 100]
[2, 12, 20, 34, 43, 45, 50, 56, 89, 100]
[2, 12, 20, 34, 43, 45, 50, 56, 89, 100]
[2, 12, 20, 34, 43, 45, 50, 56, 89, 100]
[2, 12, 20, 34, 43, 45, 50, 56, 89, 100]
[2, 12, 20, 34, 43, 45, 50, 56, 89, 100]
[2, 12, 20, 34, 43, 45, 50, 56, 89, 100]
[2, 12, 20, 34, 43, 45, 50, 56, 89, 100]
after sorting
[2, 12, 20, 34, 43, 45, 50, 56, 89, 100]
time complexity:0(N*N)
space complexity:0(1)

selection sort:
https://pastebin.com/45VXZW6D
i=int(input())
def performSelectionSort(nums):
    n = len(nums)

    for fixThisIndex in range(n - 1, 0, -1):

        maxEle = nums[fixThisIndex]
        maxEleIndex = fixThisIndex 
 
        for index in range(fixThisIndex):
            if nums[index] > maxEle:
                maxEleIndex = index 
                maxEle = nums[index]
        if fixThisIndex != maxEleIndex:
            temp = nums[maxEleIndex]
            nums[maxEleIndex] = nums[fixThisIndex]
            nums[fixThisIndex] = temp

nums =list(map(int,input().split()))

performSelectionSort(nums)

print(*nums)
#code:
def performSelectionSort(nums):
    n = len(nums)

    for i in range(n- 1, 0, -1):

        maxEle = nums[i]
        maxEleIndex = i
        for j in range(i):
            if nums[j] > maxEle:
                maxEleIndex = j 
                maxEle = nums[j]
        if i != maxEleIndex:
            temp = nums[maxEleIndex]
            nums[maxEleIndex] = nums[i]
            nums[i] = temp
 
        print(nums)

 
nums = [12, 2, 34, 20, 56, 43, 45, 100, 89, 50]
 
print("Before sorting:")
print(nums)
 
performSelectionSort(nums)
 
print("After sorting:")
print(nums)
 
o/p:
Before sorting:
[12, 2, 34, 20, 56, 43, 45, 100, 89, 50]
[12, 2, 34, 20, 56, 43, 45, 50, 89, 100]
[12, 2, 34, 20, 56, 43, 45, 50, 89, 100]
[12, 2, 34, 20, 50, 43, 45, 56, 89, 100]
[12, 2, 34, 20, 45, 43, 50, 56, 89, 100]
[12, 2, 34, 20, 43, 45, 50, 56, 89, 100]
[12, 2, 34, 20, 43, 45, 50, 56, 89, 100]
[12, 2, 20, 34, 43, 45, 50, 56, 89, 100]
[12, 2, 20, 34, 43, 45, 50, 56, 89, 100]
[2, 12, 20, 34, 43, 45, 50, 56, 89, 100]
After sorting:
[2, 12, 20, 34, 43, 45, 50, 56, 89, 100]


#INSERTION SORT;
list=[18,10,7,22,25,17]
pass1:18 is sorted list and rest elements are unsorted list
it compares the next elelment and if 18<10 then its false and it replaces in front of 18
 and now sl is updated to 18 and 10==>[10,18,7,22,25,17]
in usl we have 7,22,25,17
then it compares the last element of sl if 18<7 it is false now 10<7 it moves to left 
and then the updated sl is[7,10,18,22,25,17]
now the last element of sl i.e 18<22 i.e then it stays put then the sorted list is same
 next comparision is between 22<25i.e true next it compares 25<17i.e false then 
the sl is updated to[7,10,17,18,22,25].
https://pastebin.com/EDkZ6irM
#CODE:
def performinsertionSort(nums):
    n = len(nums)

    for i in range(1,n):
        temp=nums[i]
        pos=i-1
        while pos>=0 and nums[pos]>temp:
            nums[pos+1]=nums[pos]
            pos-=1
        nums[pos+1]=temp
        print(nums)
 
nums = [12, 2, 34, 20, 56, 43, 45, 100, 89, 50]
 
print("Before sorting:")
print(nums)
 
performinsertionSort(nums)
 
print("After sorting:")
print(nums)
 
o/p:
Before sorting:
[12, 2, 34, 20, 56, 43, 45, 100, 89, 50]
[2, 12, 34, 20, 56, 43, 45, 100, 89, 50]
[2, 12, 34, 20, 56, 43, 45, 100, 89, 50]
[2, 12, 20, 34, 56, 43, 45, 100, 89, 50]
[2, 12, 20, 34, 56, 43, 45, 100, 89, 50]
[2, 12, 20, 34, 43, 56, 45, 100, 89, 50]
[2, 12, 20, 34, 43, 45, 56, 100, 89, 50]
[2, 12, 20, 34, 43, 45, 56, 100, 89, 50]
[2, 12, 20, 34, 43, 45, 56, 89, 100, 50]
[2, 12, 20, 34, 43, 45, 50, 56, 89, 100]
After sorting:
[2, 12, 20, 34, 43, 45, 50, 56, 89, 100]
#merge sort:
the two list must be sorted.
l1=[15,18,19,25,27]
l2=[10,20,28,32,35]
the index of the 1st element of the list is pointed and the the smaller element is moved to left if any
 if same choose any one element here the  pass1 the list points to 15 and 10 next l3=[10,15,-,-,-,-,-,-,-,-]
two elements are compared at the same time
after this pass 2:15 and 20 are compared then the l3 is updated asl3=[10,15,20,-,-,-,-,-,-,-]
pass 3: 20<18 false then moved to left l3=[10,15,18,20,-,-,-,-,-,-]
pass 4:20<19then false the list is updated l3=[10,15,18,19,20,-,-,-,-,-]
pass 5:25<20 list updated l3=[10,15,18,20,25,-,-,-,-]....
similarly after n passes l3 is updated to l3=[10,15,18,19,20,25,27,28,32,35](passes:8)
look  in book
https://pastebin.com/6PFxMpMy
#code:
def merge(left,mid,right,nums):
    i1=left
    i2=mid+1
    temp=[]
    while i1<=mid and i2<=right:
        if nums[i1]>nums[i2]:
            temp.append(nums[i2])
            i2+=1
        else:
            temp.append(nums[i1])
            i1+=1
    while i1<=mid:
        temp.append(nums[i1])
        i1+=1
    while i2<=right:
        temp.append(nums[i2])
        i2+=1
    curr=0
    for pos in range(left,right+1):
        nums[pos] = temp[curr]
        curr += 1 


def divide(left,right,nums):
    print(left,'-',right)
    if left>=right:
        return 
    
    mid=(left+right)//2
    divide(left,mid,nums)
    divide(mid+1,right,nums)
    merge(left,mid,right,nums)

nums=[12,10,3,34,11,40,24]
print("before",nums)
divide(0, len(nums) - 1, nums)
print("After", nums)
o/p:
before [12, 10, 3, 34, 11, 40, 24]
0 - 6
0 - 3
0 - 1
0 - 0
1 - 1
2 - 3
2 - 2
3 - 3
4 - 6
4 - 5
4 - 4
5 - 5
6 - 6
After [3, 10, 11, 12, 24, 34, 40]

time complexity:0(NlogN)
space complexity:0(N)
the inbuilt function sorted can  be used for sorting.









