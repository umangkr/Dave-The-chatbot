import os
import random
from botReply import bot
from time import localtime, strftime
from win_text_to_speech import talk


def greet():
    x = strftime("%H", localtime())
    y = int(x)
    if y <= 12:
        greetings = 'Good morning!'
        print('dave-->>'+greetings)
        talk(greetings)
    
    elif 16 >= y >= 12:
        greetings = 'Good afternoon!'
        print('dave-->>'+greetings)
        talk(greetings)
    else:
        greetings = 'Good evening!' 
        print('dave-->>'+greetings)
        talk(greetings)

greet()
input("you-->>")  
ques = ['what can i do for you?', 'what do you want me to do?', 'how can i help you?', 'what are we doing today?']
result = random.choice(ques)
print('dave-->>'+result)

talk(result)

while 1:
    bot()
