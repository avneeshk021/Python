binary_table = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1100', '1111']
num=int(input("Enter any Number = "))
binary = ''

while(num>0):
    remainder = num%10
    binary = binary_table[remainder]+ binary
    num = num//10
    
print("binary Number: ",binary)