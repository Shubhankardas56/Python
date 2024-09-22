#adding using function:
first_no=int(input('Enter first no: '))
second_no=int(input('Enter second no: '))
def add():
    a=first_no
    b=second_no
    # print('Sum of entered two no: ',a+b)
    return a+b
add() 
print('Sum of entered two no: ',add())