n=int(input("Enter any Number ="))
if n>1:
    for i in range(2,n):
        if(n%i==0):
            print(n," is Not a prime")
            break
    else:
        print(n," Is a prime number")

elif(n==0 or n==1):
    print(n," is not prime or composite number")

else:
    print(n," is a a prime number")   