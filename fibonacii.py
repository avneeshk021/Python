istterm = 0
secondterm = 1
print("Enter the Value of n = ", end="")
n = int(input())

print("First", n, "Terms of Fibonacci Series is=")
for i in range(1, n+1):
    if (i == 1):
        istterm = 0
    elif (i== 2 or i == 3):
        istterm = 1
    else:
        secondterm = istterm
        third = secondterm
        istterm = third+secondterm
    if i == n:
        print(istterm)
    else:
        print(istterm, end=" ")