import sys
import time
import telepot
from rivescript import RiveScript

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        checkMsg(chat_id, msg['text'], msg['message_id'])

def checkMsg(chat_id, msg, id):
    m = msg.lower().split()
    res = bot.reply("localuser", msg)

    if res:
        telegram.sendMessage(chat_id, res, parse_mode='Markdown', reply_to_message_id=id)

TOKEN = sys.argv[1] 

telegram = telepot.Bot(TOKEN)
telegram.message_loop(handle)
print ('Listening ...')

bot = RiveScript()
bot.load_directory("./brain")
bot.sort_replies()

# Keep the program running.
while 1:
    time.sleep(2)

