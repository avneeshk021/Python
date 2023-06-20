num1=int(input())
num2=int(input())
if(num1>num2):
    max=num1
else:
    max=num2
while(True):
    if(num1%2==0 and num2%2==0):
        print(max)
    else:
        print("Not valid")

