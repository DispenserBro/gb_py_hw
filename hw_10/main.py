from os import getenv

from telegram import Bot
from telegram.ext import Updater

from handlers import conv_handler


TOKEN = getenv('TOKEN', 'YOUR_TOKEN')

bot = Bot(TOKEN)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()
