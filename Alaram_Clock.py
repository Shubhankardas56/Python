# importing modules here
from datetime import datetime
from playsound import playsound
#user input
Hour=int(input('set alarm Hour:'))
Min=int(input('set alarm Min:'))
ampm=str(input('set am/pm:'))
if ampm=='pm':
    Hour=Hour+12
while True:
    if (Hour==datetime.now().hour and Min==datetime.now().minute):
        playsound('E:\\PYTHON\\Python Project\\Project\\Double-beep-beep.mp3')
        playsound('E:\\PYTHON\\Python Project\\Project\\Double-beep-beep.mp3')
        playsound('E:\\PYTHON\\Python Project\\Project\\Double-beep-beep.mp3')
        playsound('E:\\PYTHON\\Python Project\\Project\\Double-beep-beep.mp3')
        playsound('E:\\PYTHON\\Python Project\\Project\\Double-beep-beep.mp3')
        playsound('E:\\PYTHON\\Python Project\\Project\\Double-beep-beep.mp3')
        playsound('E:\\PYTHON\\Python Project\\Project\\Double-beep-beep.mp3')
        playsound('E:\\PYTHON\\Python Project\\Project\\Double-beep-beep.mp3')
        break
 

        
    




