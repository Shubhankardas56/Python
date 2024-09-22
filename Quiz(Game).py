# Creating a Quiz game for Fun..
# We are creating this using Dictionary
from playsound import playsound
from time import sleep
q1='''
1)What is the maximum possible length of an identifier?
a:16
b:32
c:64
d:None of these above
'''
q2='''
2)What is the method inside the class in python language?
a:Object
b:Function
c:Attribute
d:Argument
'''
q3='''
3) Which of the following words cannot be a variable in python language?
a:_val
b:val
c:try
d:_try
'''
q4='''
4)What is the answer of '3*1**3' ?
a:27
b:1
c:3
d:0
'''
q5='''
5)What will be the output of this program?

a = ['XX', 'YY']  
for i in a:  
    i.lower()  
print(a)

a:['XX', 'YY']
b:['xx', 'yy']
c:[XX, yy]
d:None of these
'''
Question={q1:'d',q2:'b',q3:'c',q4:'c',q5:'a'} # Dictionary of questation with option
name=input('Enter your name: ')
print(f'Hello {name} welcom to the quiz world')
score=0
playsound('E:\\PYTHON\\Python Project\\Project\\Welcome.mp3')
for i in Question:
    print(i)
    playsound('E:\\PYTHON\\Python Project\\Project\\display question.mp3 ')
    ans=input('Enter your answer(a/b/c/d): ')
    if ans==Question[i]:
        print('Oh! You Enter The Correct Answer,You get a point')
        score+=1
        print(f'Your current score is:{score}')
    else:
        print('Oops! You Enter The Wrong Answer,You loose a point')
        score-=1
        print(f'Your current score is:{score}')
print() 
print(f'Your Final Score is:{score}')




