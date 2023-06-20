print("Enter a Number = ")
num = int(input('Number = '))

sum = 0
while (num!=0):
    rem = num%10
    sqr = rem*rem
    sum = sum+sqr
    num = num/10

print("Sum of squares of digits of given number is = ")
print(sum)