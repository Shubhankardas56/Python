# importaing array module
from array import array
# creating a empty array for input
Empty_Array=array('i',[])
# input array element from user
n=int(input("Enter the number of item to input:"))
# append item by using for loop
for i in range(n):
    items=int(input("Enter the items:"))
    Empty_Array.append(items)
# iterate array item using for loop
print("Array Elements are:")
for element in range(len(Empty_Array)):
    print(Empty_Array[element])