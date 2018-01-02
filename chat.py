from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
from win_text_to_speech import talk

bot = ChatBot('Test')

bot.set_trainer(ListTrainer)

for _file in os.listdir('conv'):
    chats=open('conv/'+ _file,'r').readlines()
    bot.train(chats)

def chatter(request):
    response = bot.get_response(request)
    chat_ = str(response)
    print('bot-->>'+chat_)
    talk(chat_)