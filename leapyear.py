n= int(input("Enter the year"))

if(n%400==0):

    print("Given Year is a Leap year")

elif(n%4==0 and n%100!=0):
    print ("Leap Year")

else:
    print("Is not a Leap Year")

