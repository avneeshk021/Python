octa_table = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111']
num=int(input("Enter a Binary Number = "))
octa = ''
if(num==0000):
    print("0000")
else:
 while(num>0):
    remainder = num%10
    octa = octa_table[remainder]+ octa
    num = num//10
    
print("Octa Number: ",octa)


