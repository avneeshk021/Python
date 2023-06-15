print("Enter the sides of triangle")
x=int(input("x="))
y=int(input("y="))
z=int(input("z="))

if(x==y==z):
    print("Given Triangle is Equilateral Triangle")


elif(x==y or y==z or z==x):
    print("Given Triangle is isoceles Triagnle")
else:
    print("Scalen Triangle")

