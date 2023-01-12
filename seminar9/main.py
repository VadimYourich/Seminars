import logging

from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from lesson.token_2 import token

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = token


def start(update, context):
    update.message.reply_text(
        "Привет. Выберите /calc - калькулятор\n/conv - конвертер")


def calc(update, context):
    update.message.reply_text("Введите выражение: ")
    return 1


def calculate(update, context):
    try:
        value = eval(update.message.text)
        update.message.reply_text(f'Ответ = {value}')
        return ConversationHandler.END
    except Exception as exp:
        update.message.reply_text(f'Введите правильное выражение')


def conv(update, context):
    update.message.reply_text("Введите массу в кг.: ")
    return 1


def converter(update, context):
    try:
        value = int(update.message.text)
        update.message.reply_text(f'Ответ = {value * 1000}г.')
        return ConversationHandler.END
    except Exception as exp:
        update.message.reply_text(f'Введите целое число')

    #return ConversationHandler.END  # Константа, означающая конец диалога.
    # Все обработчики из states и fallbacks становятся неактивными.


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    calc_handler = ConversationHandler(
        entry_points=[CommandHandler('calc', calc)],

        # Состояние внутри диалога.
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, calculate)],
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('conv', conv)],

        # Состояние внутри диалога.
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, converter)],
        },

        # Точка прерывания диалога. В данном случае — команда /stop.
        fallbacks=[CommandHandler('stop', stop)]
    )
    start_handler = CommandHandler('start', start)

    dp.add_handler(start_handler)
    dp.add_handler(calc_handler)
    dp.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
