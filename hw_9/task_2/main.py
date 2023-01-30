from os import getenv

from telegram import Bot, Update
from telegram.ext import (Updater,
                          CommandHandler,
                          MessageHandler,
                          Filters,
                          CallbackContext,
                          ConversationHandler)


TOKEN = getenv('TOKEN', '5860877963:AAH3xK3QgIi9hqa971YVEHamMLovPt2yTNk')
STATES = (0, 1)
DEFAULT_CANDIES = 120
MAX_CANDIES = 28

candies = DEFAULT_CANDIES
is_bot = False

bot = Bot(TOKEN)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher


def tg_out(text, chat_id, context: CallbackContext):
    context.bot.send_message(chat_id, text)


def smart_bot_move(candies_cnt: int,
                   player_candies: int,
                   max_candies: int = 28) -> int:
    if candies_cnt - max_candies < 1:
        return max_candies + (candies_cnt - max_candies)

    if candies_cnt - player_candies > max_candies:
        return player_candies

    if candies_cnt <= max_candies * 2:
        res_value = candies_cnt - (max_candies + 1)
        return res_value if res_value else max_candies

    return max_candies


def check_candies(candies_cnt: int,
                  took_candies: int,
                  chat_id: int,
                  context: CallbackContext,
                  max_candies: int = 28) -> bool:
    if (took_candies > max_candies) or (took_candies < 1):
        tg_out(f'Конфеты можно брать только в диапазоне [1-{max_candies}]!',
               chat_id,context)
        return False

    if took_candies > candies_cnt:
        tg_out('На столе осталось меньше конфет!',
               chat_id, context)
        return False

    return True


def start(update: Update, context: CallbackContext) -> int:
    tg_out('Привет\nЯ бот для игры в конфеты',
           update.effective_chat.id, context)
    tg_out(f'На столе {candies} конфет',
           update.effective_chat.id, context)
    tg_out(f'Введи количество конфет [1-{MAX_CANDIES}]',
           update.effective_chat.id, context)
    return STATES[0]


def game(update: Update, context: CallbackContext):
    global candies, is_bot

    candies_limit = MAX_CANDIES if candies >= MAX_CANDIES else candies

    took_candies = int(update.message.text)

    if not check_candies(candies, took_candies,
                         update.effective_chat.id,
                         context, candies_limit):
        tg_out(f'Введи количество конфет [1-{candies_limit}]',
               update.effective_chat.id, context)

        return STATES[0]

    is_bot = False
    candies -= took_candies

    tg_out(f'Ты взял {took_candies} конфет, осталось {candies}',
           update.effective_chat.id, context)

    if candies:
        is_bot = True

        took_candies = smart_bot_move(candies, took_candies, candies_limit)
        candies -= took_candies

        tg_out(f'Я взял {took_candies} конфет, осталось {candies}',
               update.effective_chat.id, context)

    if not candies:
        tg_out(['Ты выиграл!', 'Выиграл я!'][is_bot],
               update.effective_chat.id, context)
        tg_out('Хочешь снова сыграть?\nВведи "да", "y" или "yes"',
               update.effective_chat.id, context)

        return STATES[1]

    tg_out(f'Введи количество конфет [1-{candies_limit}]',
               update.effective_chat.id, context)

    return STATES[0]


def restart_game(update: Update, context: CallbackContext):
    global candies

    candies = DEFAULT_CANDIES
    decision = update.message.text

    if decision.lower() not in ('да', 'y', 'yes'):
        tg_out('Спасибо за игру!', update.effective_chat.id, context)
        return ConversationHandler.END

    tg_out('Перезапуск игры...', update.effective_chat.id, context)
    tg_out(f'На столе {candies} конфет',
           update.effective_chat.id, context)
    tg_out(f'Введи количество конфет (1-{MAX_CANDIES})',
           update.effective_chat.id, context)
    return STATES[0]


def cancel(update: Update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, 'Прощай!!!')


start_handler = CommandHandler('start', start)
game_handler = MessageHandler(Filters.text, game)
restart_handler = MessageHandler(Filters.text, restart_game)
cancel_handler = CommandHandler('cancel', cancel)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={STATES[0]: [game_handler],
                                   STATES[1]: [restart_handler]},
                                   fallbacks=[cancel_handler])

dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()