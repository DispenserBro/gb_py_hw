from os import getenv

from telegram import Bot, Update
from telegram.ext import (Updater,
                          CommandHandler,
                          MessageHandler,
                          Filters,
                          CallbackContext)


TOKEN = getenv('TOKEN', '5860877963:AAH3xK3QgIi9hqa971YVEHamMLovPt2yTNk')

bot = Bot(TOKEN)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher


def start(update: Update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, 'Привет!\n\
Пришли мне сообщение, и я удалю из него слова,\n\
в которых содежится "абв"')


def text_messages(update: Update, context: CallbackContext):
    msg_text = update.message.text.split()
    text_to_send = [el for el in msg_text if not 'абв' in el]
    text_to_send = ' '.join(text_to_send) if text_to_send else 'Слова закончились :)'
    context.bot.send_message(update.effective_chat.id, text_to_send)


start_handler = CommandHandler('start', start)
message_handler = MessageHandler(Filters.text, text_messages)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()