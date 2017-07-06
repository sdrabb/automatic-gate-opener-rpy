import sys
import os
import telepot
import datetime
import time
from remote_controller import toggle_relay

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
        if command == '/toggle':
            bot.sendMessage(chat_id, 'toggle gate')
	    toggle_relay(18)
    else:
        bot.sendMessage(chat_id, 'you are not authorized, please ask super user')
        bot.sendMessage(chat_id, sender)

if __name__ == "__main__":
    bot = telepot.Bot('***** PUT YOUR TOKEN HERE *****')
    print(bot.getMe())
    bot.message_loop(handle)
    print 'I am listening ...'

    while 1:
        time.sleep(10)
