str=input('Enter a string: ')
vow='aeiouAEIOU'
list=[]
for i in str:
    if i in vow:
        list.append(i)
if set(list)==set():
    print(f'{str} have no vowle')
else:
    print(f' from {str} vowles are {set(list)}')