x=int(input("Enter two number="))
y= int(input("Enter two Number="))

if(x>0 and y>0):
    print("Coordinates belongs to 1st Quardent")
elif(x<0 and y>0):
    print("Coordinates belongs to 2nd Quardent")
elif(x<0 and y<0):
    print("Coordinates belongs to 3rd Quardent")
else:
    print("Coordinates belongs to 4rd Quardent")