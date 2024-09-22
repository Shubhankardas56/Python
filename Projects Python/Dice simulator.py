from random import randrange
dice_num=[1,2,3,4,5,6]
while True:
    dice_num_input=int(input('choose a num from the dice(1 to 6): '))
    if dice_num_input in dice_num:
        random_dice_num=randrange(1,7)
        if dice_num_input==random_dice_num:
            print('congratulation!! You got the same number as u expect')
        elif dice_num_input in range(1,4):
            print('you are too close,keep trying')
        elif dice_num_input in range(4,7):
            print('you are faraway from your dice call')
        else:print('Enter a valid number from 1 to 6 ')