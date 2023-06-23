file =open("C:\\Users\\hp\\OneDrive\\Desktop\\filehandling\\hello.txt","w+")
file.write("hii")
print("hello")  #this function is used to write something in our  file
file.read()
file.close()

file =open("C:\\Users\\hp\\OneDrive\\Desktop\\filehandling\\hello1.txt","r")
print(file.read())
file.close()
