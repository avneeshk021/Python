x=float(input("Enter base number="))
n= int(input("Enter power number="))
sum=1
for i in range(1,n+1):
    if(i%2==0):
        sum=sum+ x**i
    else:
        sum=sum- x**i

    

print("Sum of the series is =",sum)
