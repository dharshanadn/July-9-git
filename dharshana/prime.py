n=int(input("enter the num:"))
isprime = True
if n>1:
  for i in range(2,n):
    if(n%i)==0:
     isprime = False
     break
  
  if(isprime):
    print("prime")
  else:
     print("not a prime")



 