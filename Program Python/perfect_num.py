num=int(input('Enter a number: '))
n=0
for i in range(1,num):
    if num%i==0:
        n+=i
if n==num:
    print(f'{num} is a perfect number')
else:
    print(f'{num} is not a perfect number')