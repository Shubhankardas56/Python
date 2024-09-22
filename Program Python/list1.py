#creating a list
lis=["rahul","raj","rohit",21,54]
lis1=['babul',43]
lis2=[45,23,10,78]
#accessing a list
print(lis[0])
print(lis[1])
print(lis[2])
print(lis[3])
print(lis[4])
print(lis[-1])
print(lis[-2])
print(lis[-3])
print(lis[-4])
print(lis[-5])
print()
#sclicing a list
print()
print(lis[1:-1])
print(lis[1:-1:2])
print(lis[2::2])
print(lis[::])
print(lis[::-1])
print(lis[::-2 ])
print(lis[::-3 ])
print(lis[1::-1])
#change item from the list
print()
lis[0]="rajkumar"
lis[1]="rajib"
lis[2]=45
lis[3]="rakesh"
lis[4]=34
print(lis)
#adding element to list(append,extend)
lis.append(12)
print(lis)
lis.append("raji")
print(lis)
print()
lis.append((12,16,'raj'))
print(lis)
lis.extend((12,16,'raj'))
print(lis)
#adding using + and * operator
print()
new_lis=lis+lis1
print(new_lis)
s=lis1*6
print(s)
#adding element in a certain position
print()
lis.insert(1,"raju rastogi")
print(lis)
lis.insert(2,'maha raj')
print(lis)
print()
print()
#removing items from the list
lis.remove('rakesh')
print(lis)
lis.remove('rajib')
print(lis)
#removing last item from a list(pop)
lis.pop()
print(lis)
#removing a particular item from a list
lis.pop(6)
print(lis)
lis.pop(6)
print(lis)
lis.pop(5)
print(lis)
#removing item using del method
del lis[2]
print(lis)
#reversing a list
lis.reverse()
print(lis)
#shorting element in a list
lis2.sort()
print(lis2)
#we can copy one list to another using .copy() method
lis3=lis1.copy()
print(lis3)
# iterating item form the list
print()
for i in lis:
    print(i)
    print()
for i in lis1:
    print(i)
    print()
for i in lis2:
    print(i)
#clear all the item from a list
print()
lis.clear()
print(lis)
lis1.clear()
print(lis1)
lis2.clear()
print(lis2)
print()
#deleting the entire list
del lis
print(lis)