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