num=int(input('Enter nth term: '))
n1=0
n2=1
count=0
if num<=0:
    print('Enter a positive number')
elif num==1:
    print(f'{num}th term is {n1}')
else:
    while count<num:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
    