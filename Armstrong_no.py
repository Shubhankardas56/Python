num=int(input('Enter a number: '))
copy_num=num
pow=len(str(num))
sum=0
while(num>0):
    dig=num%10
    sum+=dig**pow
    num=num//10
if (sum==copy_num):
    print(f'{copy_num} is a armostrang no')
else:
    print(f'{copy_num} is not a armostrang no')