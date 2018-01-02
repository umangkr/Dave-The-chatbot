import os
import random
from datetime import datetime
from joke import joke
from chat import chatter
from win_text_to_speech import talk
import time


def bot():
    arg = input('you-->>')
    if 'shopping' in arg or 'shop' in arg:
        sites = ['https://www.flipkart.com/', 'https://www.amazon.in/', 'https://www.snapdeal.com/']
        talk('here you go')
        os.startfile(random.choice(sites))
        

    elif 'music' in arg or 'musics' in arg or 'songs' in arg or 'song' in arg:
        print('dave-->>which song would you like to listen?')
        talk('which song would you like to listen?')
        song = input('you-->>')
        if 'nothing' in song or 'none' in song or 'leave' in song:
            print('dave-->>okay')
            talk('okay')

            

        else:
            print('dave-->>here you go')
            talk('here you go')
            os.startfile('https://gaana.com/search/' + song)

            

    elif 'video' in arg or 'videos' in arg:

        list1 = ['what would you like to watch?', 'okay! which video?']
        x = random.choice(list1)
        print('dave-->>'+x)
        talk(x)
        song = input('you-->>')
        if 'nothing' in song or 'none' in song or 'leave' in song:
            print('dave-->>okay')
            talk('okay')

            
        else:
            print('dave-->>here you go')
            talk('here you go')
            os.startfile('https://www.youtube.com/results?search_query=' + song)

            

    elif 'meaning' in arg:
        print('dave-->>okay')
        talk('okay')
        os.startfile('https://www.google.co.in/search?hl=en&source=hp&ei=yd_-WbnxAYnWvATq34GgAg&q=' + arg)
        

    elif 'mail' in arg or 'email' in arg or 'mails' in arg or 'emails' in arg:
        print('dave-->>which email service?')
        talk('which email service')
       
        mails = input('you-->>')
        if 'nothing' in mails or 'leave' in mails or 'none' in mails:
            print('dave-->>okay')
            talk('okay')
            

            
        else:
            print('dave-->>okay! here are your mails')
            talk('okay! here are your mails')
            
            if 'yahoo' in mails:
                os.startfile('https://login.yahoo.com/?.src=ym&.intl=in&.lang=en-IN&.done=https%3A%2F%2Fin.mail.yahoo.com%2F')
    
                
            elif 'gmail' in mails or 'Gmail' in mails:
                os.startfile('https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    
                
            else:
                print('dave-->>sorry could not understand it')
                talk('sorry could not understand it')
                
    
                
    elif 'location' in arg or 'locate' in arg or 'situated' in arg:
        print('dave-->>okay, here it is')
        
        talk('okay here it is')
        os.startfile('https://www.google.co.in/maps/place/'+ arg)
        

    elif 'near' in arg:
        print('dave-->>here are some places')
        
        talk('here are some places')
        os.startfile('https://www.google.co.in/maps/search/places+near+me/@26.815739,80.8967841,13z/data=!3m1!4b1')
        

    elif 'date' in arg or 'time' in arg:
        x = str(datetime.now())
        print(datetime.now())
        talk(x)
        

    elif 'quit' in arg or 'nothing' in arg or 'bye' in arg or 'goodbye' in arg or 'ciao' in arg or 'exit' in arg:
        print('dave-->>i am glad i could help you')
        talk('i am glad i could help you')
        print('dave-->>bye! have a nice day')
        talk('bye have a nice day')
        exit()

    elif 'joke' in arg:
        joke()
        

    elif 'who are you' in arg:
        print('dave-->>i am dave.')
        talk('i am dave')
        print('dave-->>i am a digital assistant built to help you when you need my help')
        talk('i am a digital assistant built to help you when you need my help')
        

    elif 'bored' in arg or 'boring' in arg:
        print('dave-->>would you like to go out?')
        talk('would you like to go out?')
        a=input('you-->>')
        if a == 'yes' or a == 'okay' or a == 'ok':
            print('dave-->>okay! here are some events near by you')
            talk('okay here are some events near by you')
            
            os.startfile('https://in.bookmyshow.com/lucknow')

            

        else:
            print('dave-->>okay! would you like to watch videos?')
            talk('okay! would you like to watch videos?')
        
            inp = input('you-->>')
            if inp == 'ok' or inp == 'yes' or inp == 'okay':
                print('dave-->>here you go')
                talk('here you go')
                
                os.startfile('https://www.youtube.com/')
    
                

            else:
                print('dave-->>sorry i am unable to help you')
                talk('sorry i am unable to help you')
                
    
                

    elif 'weather' in arg:
        print('dave-->>let me check')
        talk('let me check')
        
        os.startfile('https://www.accuweather.com/en/in/india-weather')
        

    elif 'note' in arg:                            
        os.system('start notepad')
        
    elif 'travel' in arg or 'trip' in arg or 'journey' in arg or 'ticket' in arg:
        print('dave-->>okay how would you like to travel by train or plane?')
        talk('okay how would you like to travel by train or plane?')
        _inp=input("you-->>")
        if 'train' in _inp:
            print('dave-->>okay! here you go')
            talk('okay here you go')
            
            os.startfile('https://www.irctc.co.in/eticketing/loginHome.jsf')
        elif 'plane' in _inp or 'flight' in _inp:
            print('dave-->>okay! here you go')
            talk('okay here you go')
            os.startfile('https://www.cleartrip.com/flights')
        else:
            print('dave-->>sorry could not complete request')
            talk('sorry could not complete request')
            

    elif 'hotel' in arg or 'check in' in arg or 'stay in' in arg:
        print('dave-->>okay! here you go')
        talk('okay here you go')
        
        os.startfile('https://www.trivago.in')

    else:
        chatter(arg)


