hexa_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
num=int(input("Enter any Number = "))
hexadeci = ''

while(num>0):
    remainder = num%16
    hexadeci = hexa_table[remainder]+ hexadeci
    num = num//16
    
print("Hexadecimal Number: ",hexadeci)

# ans=[]
# dic={10:'a',11:'b' ,12:'c' ,13:'d' ,14:'e' ,15:'f'}
# if(num==0):
#     print("0")
# if(num<0):
#     num=num+2**32
# while(num>0):
#     dig=num%16
#     num=num//16
#     if(dig>9 and dig<16):
#         dig=dic[dig]
#     else:
#         dig=dic
