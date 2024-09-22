from array import array
stu_data=array('i',[101,102,103,104,105])

# accessing array
for element in stu_data:
    print(element)

# accessing  array using length function
print() 
n=len(stu_data)
for i in range(n):
    print(stu_data[i])

# accessing array using while loop
print()
n=len(stu_data)
i=0
while i<n:
    print(stu_data[i])
    i+=1 
 

