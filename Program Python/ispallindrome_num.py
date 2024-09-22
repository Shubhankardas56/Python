num=int(input('Enter a number: '))
rev=0
b=num
while num>0:
    dig=num%10
    rev=rev*10+num%10
    num=num//10
if b==rev:
    print(f'{b} is a pallindrom number')
else:
    print(f'{b} is not a pallindrom number')