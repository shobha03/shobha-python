1.WAPto add key value pair to dictionary?

details={}
key=input("enter the  key:")
value=input("enter the value:")
details[key]=value
d1={"rollno":524}
details.update(d1)
details.setdefault("branch","cse")
print(details)

output::
C:\Users\Sobha\Desktop>chec.py
enter the  key:name
enter the value:shobha
{'name': 'shobha', 'rollno': 524, 'branch': 'cse'}

2.WAP TO concate two strings into one?
d1={"name":"shobha","roolno":524}
d2={"barnch":"cse","course":"python"}
d1.update(d2)
print(d1)

output::
C:\Users\Sobha\Desktop>chec.py
{'name': 'shobha', 'roll': 524, 'branch': 'cse', 'course': 'python'}

3.WAPto check whther key is exist or not in dicitionary?

d1={"name":"shobha","roolno":524}
if("name" in d1):
   print("yes")

   output::
   C:\Users\Sobha\Desktop>chec.py
yes

or

def check(dict,key):
   if key in dict:
      print("yes",end="")
dict={"a":1,"b":2}
key="a"
check(dict,key)

4.WAP TO remove given key in from dictionary?

d1={"name":"shobha","branch":"cse","age":21}
print(d1)
d1.pop("name")
print(d1)

output::
C:\Users\Sobha\Desktop>chec.py
{'name': 'shobha', 'branch': 'cse', 'age': 21}
{'branch': 'cse', 'age': 21}

5.WAp to map two list of items into dictionary?

d1=["name","branch","age"]
d2=["shobha","cse",21]
dictionary=dict(zip(d1,d2))
print(dictionary)

output:;
C:\Users\Sobha\Desktop>chec.py
{'name': 'shobha', 'branch': 'cse', 'age': 21}

6. to count the frequence of words apperaing in astring using disctionary?

words=input().split()
wordscount1={}
print(len(words))
for word in words:
   wordscount1[word]=words.count(word)
print(wordscount1)
for k,v in wordscount1.items():
    print(k,":",v)

    output::
    10
{'haii': 1, 'iam': 2, 'shobha': 1, 'and': 2, 'from': 1, 'hyd': 1, 'iwant': 1, 'to': 1}
haii : 1
iam : 2
shobha : 1
and : 2
from : 1
hyd : 1
iwant : 1
to : 1

7.WAP to create adict with key asa first character and values as word starting with that character?

words=input().split()
wordscount1={}
print(len(words))
for word in words:
   if(word[0]not in wordscount1.keys()):
      wordscount1[word[0]]=[]
      wordscount1[word[0]].append(word)
for k,v in wordscount1.items():
    print(k,":",v)

    output::
    C:\Users\Sobha\Desktop>chec.py
haii iam shobha and iam from hyd and i want to
11
h : ['haii']
i : ['iam']
s : ['shobha']
a : ['and']
f : ['from']
w : ['want']
t : ['to']

8.WAP togenerate dictionary that contains conains number in the form(x,x*x)?
sqrs={}
n=int(input("enter the values 1:"))
for i in range(1,n+1):
    sqrs[i]=pow(i,2)
    print(sqrs)

    output::

C:\Users\Sobha\Desktop>chec.py
enter the values 1:10
{1: 1}
{1: 1, 2: 4}
{1: 1, 2: 4, 3: 9}
{1: 1, 2: 4, 3: 9, 4: 16}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
