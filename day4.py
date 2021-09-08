1.find evens in between range along with count and sum?

i=2
def even(i):
 sum=0
 count=0
 for i in range(1,20):
    if(i%2==0):
       print("the number is even:",i)
       sum=sum+i
       count+=1
       print("the sum of even numbers is:",sum)
       print("the number is between 20 is:",count)
print(even(i))

2.find given number is prime or not?

n =int(input("enter number"))
x=0
if(n>1):
  for i in range(2,n):
       if(n%i==0):
         x+=1
    if(x==0):
      print(n,"is a prime number")
    else:
      print(n,"is a prime number")


  3.print primes in a given range then print count and sum also ?

  a=int(input("enter a number"))
def isprime(x):
  count=0
  sum=0
  for b in range(2,x+1):
     for i in range(2,b):
        if(b%i==0):
           break
     else:
           print(b,end='')
           count+=1
           sum=sum+b
           print("is prime number")
           print("count of prime numbers in between range:",count)
           print("sum of prime numbers in between range:",sum)
print(isprime(a))

4.print primes in a given range then print count ?

a=int(input("enter a number"))
def isprime(x):
  count=0
  for b in range(2,x+1):
     for i in range(2,b):
        if(b%i==0):
           break
     else:
           print(b,end='')
           count+=1
           print("is prime number")
           print("count of prime numbers in between range:"count)
           print(isprime(a))
