# Number= int(input("Enter the digit which Yor Want="))
# sum=0
# while Number!=0:
#     digit=int(Number%10)
#     sum+=digit
#     Number=Number/10
#     print(sum)
num='105'
reverse=''
for i in range(len(num), 0,-1):
    reverse+=num[i+1]
print('reverse number =',reverse)