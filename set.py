set={1,2,5,6,7,4,9} #We can  not change value in set
set2={'A', 'B', 'C', 'D', 'E','F', 'G'}
print(set)
print(type(set))
print(len(set))
#for loop
for i in set:
    print(i," ",end='')
    #membership 
print(1 in set )
#HERE WE USE ADD FUCTION
set.add("A")
print(set)
#HERE WE USE UPADTE FUCTION
set.update(set2)
print(set)
 #HERE WE USE REMOVE FUCTION
set.remove("A")
print(set)
#HERE WE USE Discard FUCTION
set.discard("B")
print(set)
#HERE WE USE POP FUCTION
set.pop()
print(set)
#HERE WE USE clear FUCTION
# set.clear()
# print(set)
#here we use union function
set.union(set2)
print(set)


