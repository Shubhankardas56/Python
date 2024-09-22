num=int(input('Enter a num: '))
pow=len(str(num))
copy_num=num
sum=0
while num>0:
    dig=num%10
    sum=sum+dig**pow
    num=num//10
if sum==copy_num:
    print(f'{copy_num} is a armstrong number ')
else:
    print(f'{copy_num} is not a armstrong number')