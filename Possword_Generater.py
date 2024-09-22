from random import choice,shuffle
pass_length=int(input("Enter the length of your password to generate:"))
while True:
    # list of capital alphabet
    list_of_capital_alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    # list of small alphabet
    list_of_small_alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    # list of special symbol alphabet
    list_of_special_item=["@","#","$","&"]
    # list of number
    list_of_number=[1,2,3,4,5,6,7,8,9]
    total_type=list_of_capital_alphabet+list_of_small_alphabet+list_of_special_item+list_of_number
    print('Random generated password is: ',end='')
    for i in range(pass_length):
        rand=choice(total_type)
        print(rand,end="")
    break
    

    


    


