# character is digit or alphabet or symbol
char=input('enter a single character: ')
if char.isdigit():
    print('entered character is a digit')
elif char.isalpha():
    print('entered character is a alphabet')
else:
    print('entered character is a specialsymbool')