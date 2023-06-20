n=int(input("Enter the number="))
temp=n
sum=0
while(temp>0):
    dig=temp%10
    sum=sum+dig*dig*dig
    temp//=10
if(n==sum):
    print("NUmber is Armgstong Number")

else:
    print("Number is not a Armgstong Number")

    
