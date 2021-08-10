n=int(input("enter a number:"))
is_prime=True
for i in range(1,n):
   
    if n%i==0:
        is_prime==False
    
if is_prime==True:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
    
    