# activity 3 Python Function to check the number is prime or not
n=int(input("Enter number: ")) 
k=0 
for i in range(2,n//2+1): 
    if(n%i==0): 
        k=k+1 
if(k<=0): 
    print("Your number is a prime number") 
else: 
    print(" Your number is not a prime number") 