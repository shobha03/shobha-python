1.write a program to find the largest number in list?
list=[2,1,6,7]
print("longest number in list:",max(list))

solu::
C:\Users\Sobha\Desktop>max.py
longest element in list: 7

2.write a program to find the  second largest number in list?

l=[2,1,6,7]
l.sort()
print("the list is:",l)
print(" second largest element in list:",l[2])

 solu::
C:\Users\Sobha\Desktop>max.py
the list is: [1, 2, 6, 7]
 second largest element in list: 6

       or
list=[2,1,6,7]
new_list=set(list)
new_list.remove(max(new_list))
print("the list is:",list)
print(" second largest element in list:",max(new_list))

3.write aprogram to put even and odd elements in a list into different lists?
 a=[]
n=int(input("enter the number of elements"))
for j in range(1,n+1):
     b=int(input("enter the  elements"))
     a.append(b)
even=[]
odd=[]
for i in a:
     if(i%2==0):
       even.append(i)
     else:
       odd.append(i)
print("even numbers list:",even)
print("the odd list:",odd)

C:\Users\Sobha\Desktop>even.py
enter the number of elements5
enter the  elements8
enter the  elements9
enter the  elements3
enter the  elements2
enter the  elements1
even numbers list: [8, 2]
the odd list: [9, 3, 1]

4.write aprogram to remove the uplicate item in list?
list1=[1,23,12,1,3]
set1=set(list1)
list2=list(set1)
print(list2)

output:
C:\Users\Sobha\Desktop>duplicate.py

5.write a program to remove asecond occurance word  in list wehre words can repeate?
l=["haii","how","haii"]
for j in l:
   if(l.count("i")==2):
       print("remove of second occurance element:",l.remove("haii"))

print(j)

output::
C:\Users\Sobha\Desktop>remove.py
remove of second occurance element: None
haii


6 .WAP to program to findall numbers in a ramge which are perfect squares and sum of all digits lessthen 10?

import math
sum=0
a=[1,2,4]

for i in a:
    root=math.sqrt(i)
    sum=sum+i
if int(root+0.5)**2==i:
     print("perfect number:",i)

elif(sum<10):
    print("sum of digits is less then 10",)

output::
C:\Users\Sobha\Desktop>max.py
perfect number: 4
sum of digits is less then 10
