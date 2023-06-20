a = int(input("Enter First Number of an A.P Series= "))
n = int(input("Enter teh Total Numbers in dis A.P Series= "))
d = int(input("Enter teh Common Difference ="))

total = (n * (2 * a + (n - 1) * d)) / 2
tn = a + (n - 1) * d

print("The Sum of Arithmetic Progression Series = " , total)
print("Teh tn Term of Arithmetic Progression Series = " , tn)