a=int(input("Enter the first Number of Series="))
n = int(input("Enter teh Total Numbers in G.P Series= "))
r = int(input("Enter teh Common Difference ="))

for i in range(1,n+1):
    tn= a*(r**(n-1))
    print(tn)

sum=0
sn=(a*(r**n))/(r-1)
if(r>1):
    print("Sum=",sn)
else:
    print("Sum ", sn)
    3