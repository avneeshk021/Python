print("Enter a Number: ")
num = int(input('Number = '))

rev = 0
while (num!=0):
  rem = num%10
  rev = rem + (rev*10)
  num = num/10

print("Reverse =", rev)