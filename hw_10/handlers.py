from telegram import Update
from telegram.ext import (CommandHandler,
                          MessageHandler,
                          Filters,
                          CallbackContext,
                          ConversationHandler)

from calculator import process_func
from logger import log, get_logs


STATES = (0, 1, 2)

def start(update: Update, context: CallbackContext) -> int:
    context.bot.send_message(update.effective_chat.id,
                             'Привет, я бот-калькулятор!')
    context.bot.send_message(update.effective_chat.id,
                             'Выбери действие:\n\t1. Калькулятор\
\n\t2. Последние действия\nЛюбой другой ввод выходит из дилаога!')
    return STATES[0]


def menu(update: Update, context: CallbackContext) -> int:
    msg_data = update.message.text

    if msg_data == '1':
        context.bot.send_message(update.effective_chat.id,
                                 'Ты выбрал калькулятор\n\
Введи выражение без скобок и отрицательных чисел\nНапример: 2+3*6')
        return STATES[1]

    elif msg_data == '2':
        context.bot.send_message(update.effective_chat.id,
                                 'Ты выбрал просмотр последних действий\n\
Введи количество записей, которые ты хочешь посмотреть')
        return STATES[2]

    else:
        context.bot.send_message(update.effective_chat.id,
                                 'Спасибо за пользование!')
        return ConversationHandler.END


def calculator(update: Update, context: CallbackContext) -> int:
    user_id = update.effective_user.id
    username = update.effective_user.username
    if username:
        username = '@' + username

    msg_data = update.message.text

    result = str(process_func(msg_data))

    context.bot.send_message(update.effective_chat.id, f'Результат: {result}')
    # update.effective_message.reply_text()
    log(user_id, username, msg_data, result)

    context.bot.send_message(update.effective_chat.id,
                             'Выбери действие:\n   1. Калькулятор\
\n   2. Последние действия\n\nЛюбой другой ввод выходит из дилаога!')

    return STATES[0]


def last_logs(update: Update, context: CallbackContext) -> int:
    logs_cnt = int(update.message.text)
    logs = get_logs()
    if logs:
        cols = logs[0]
        logs = logs[1:]
    
    if logs_cnt > 0 and logs_cnt <= len(logs):
        for log in logs[-logs_cnt:]:
            msg_text = []

            for i in range(len(log)):
                msg_text.append(f'{cols[i]}: {log[i]}')

            msg_text = '\n'.join(msg_text)
            context.bot.send_message(update.effective_chat.id, msg_text)

    if len(logs) < 1:
        context.bot.send_message(update.effective_chat.id,
                                 'В логах пока нет записей!')

    elif logs_cnt > len(logs):
        context.bot.send_message(update.effective_chat.id,
                                 f'В логах всего {len(logs)} записей!')

    context.bot.send_message(update.effective_chat.id,
                             'Выбери действие:\n\t1. Калькулятор\
\n\t2. Последние действия\nЛюбой другой ввод выходит из дилаога!')

    return STATES[0]


def cancel(update: Update, context: CallbackContext):
    context.bot.send_message(update.effective_chat.id, 'Пока!!!')


start_handler = CommandHandler('start', start)
menu_handler = MessageHandler(Filters.text, menu)
calculator_handler = MessageHandler(Filters.text, calculator)
last_logs_handler = MessageHandler(Filters.text, last_logs)
cancel_handler = CommandHandler('cancel', cancel)

conv_handler = ConversationHandler(entry_points=[start_handler],
                                   states={
                                       STATES[0]: [menu_handler],
                                       STATES[1]: [calculator_handler],
                                       STATES[2]: [last_logs_handler]
                                   },
                                   fallbacks=[cancel_handler])
