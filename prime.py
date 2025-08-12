def is_prime(num):
    if num <= 1:
        return False
    for i in range (2,int(num**0.5)+1):
        if num % i == 0 : 
            return False
        return True
        print()
limit = int(input("Enter the limit for the prime number: "))
print(limit)        


# right pyrmaid traingle 
n = int(input("enter a number:"))
for i in range (1,n-1):
    for j in range(1,i+1):
        print("*",end ="")
        print()
        