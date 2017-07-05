import sys
import os
import telepot
import datetime
import time

"""
Ctrl-C per uscire.
"""

#contains chat id authorized to chat with the bot
id_a = [21219501, 2222222, 3333333, 4444444, 5555555]


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    sender = msg['from']['id']

    print 'Got command: %s' % command

    if sender in id_a:
        if command == '/open':
            bot.sendMessage(chat_id, 'gate opening')

    else:
        bot.sendMessage(chat_id, 'you are not authorized, please ask super user')
        bot.sendMessage(chat_id, sender)


bot = telepot.Bot('***** PUT YOUR TOKEN HERE *****')
print(bot.getMe())
bot.message_loop(handle)
print 'I am listening ...'

while 1:
    time.sleep(10)