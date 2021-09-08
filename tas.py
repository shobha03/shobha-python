1.name=input("enter name")
name=name.replace("a","$")
print(name)



2.s1=input("enter string1")
s2=input("enter string2")
if(len(s1)==len(s2)):
     for ch in s1:
        if ch in s2:
            continue
        else:
           print("it is  anagram")
else:
   print("it not anagram")



a=input("enter the string:")
x=a[0]
y=a[1:-1]
z=a[-1]
print(x+y+z)


x=input("enter the string")
count=0
y=a.lower()
for ch in x:
   if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
          count+=1
print(count)



x="python programing"
print(x.replace("","-"))


x="python programing"
count=0
for ch in x:
   count+=1
print(count)


x="python programing"
print(len(x))



x="python programing"
y=x.split()
count=0
for i in y:
    count+=1
print("number of words:", count)
count=0
for i in x:
    count+=1
print("number of characters:", count)



x=input("enter the string1")
y=input("enter the string2")
count1=0
count2=0
for i in x:
   count1+=1
for j in y:
    count2+=1
if(count1>count2):
   print("the larger one is:",x)
else:
   print("the larger one is:",y)



a="ConzurA Soft Solutions"
count=0
for ch in a:
    if(ch.islower()==True):
       count+=1
print(count)



x=input("enter string:")
y=x[::-1]
if(x==y):
   print(x,"is a palindrom")
else:
   print(x,"is not a palindrom")




x="Conzura SOft Solutions"
count1=0
count2=0
for i in x:
   if(i.isupper()==True):
      count1+=1
   if(i.islower()==True):
    count2+=1
   print("upper case letters:",count1)
   print("lower case letters:",count2)




s=input("enter the string")
dcount=0
lcount=0
for ch in s:
   if ch.isdigit():
       dcount +=1
   elif(ch.isalpha()):
       lcount +=1
   else:
      pass
print("digit count is :",dcount)
print("letter count is:",lcount)





a=input("enter the string")
x=a[0:2]
y=a[-2:]
print(x+y)





a="hello man how are"
b=a.split()
c=[]
for i in b:
    if(i not in c):
       c.append(i)
for i in range(0,len(c)):
    print("occurance of",c[i],"is:",b.countc[i])





a=input("enter substring:")
b="hello nice meeting you"
if(a in b):
  print("substring is:",a)
else:
  print("substring is not:",a)




x=input("enter:")
sum=0
for ch in x:
    if ch.isdigit():
       sum +=int(ch)
print(sum)
