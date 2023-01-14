import logging

from random import randint
from token_1 import *
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters

reply_keyboard = [['/play ▶️', '/rules 📝'],
                  ['/settings ☑️', '/close ⏹️']]
reply_keyboard2 = [['/close ⏹️', '/rules 📝']]

candies = 50
step = 15
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=False, resize_keyboard=True)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = token


def start(update, context):
    #name = f"{update.message.from_user.ferst_name} {update.message.from_user.last_name}"    -- у меня не работает с этой строкой, не могу разобраться
    context.bot.send_photo(update.effective_chat.id, photo=open('icon-256x256.png', 'rb'))
    update.message.reply_text(
        f"Привет! Сыграем? Выбери нужный пункт меню:", # {name} здесь тоже убрал
        reply_markup=markup
    )


def close_keyboard(update, context):
    update.message.reply_text(
        "До встречи!",
        reply_markup=ReplyKeyboardRemove()
    )


def rules(update, context):
    update.message.reply_text(
        "Сначала нужно определить количество конфет на кону и количество конфет, "
        "которое можно взять за один раз.")


def settings(update, context):
    update.message.reply_text("Введите количество конфет на кону и максимально "
                              "возможное количество на ход через пробел: ", reply_markup=markup2)
    return 1


def set_settings(update, context):
    global candies
    global step
    candies, step = map(int, update.message.text.split())
    update.message.reply_text("Правила установлены, начинаем!", reply_markup=markup2)
    return ConversationHandler.END


def play(update, context):
    update.message.reply_text(f"На кону {candies} конфет. Ваш ход. Какое количество конфет вы берете?"
                              f"(Доступно {step} конфет)", reply_markup=markup2)
    return 1


def play_step(update, context):
    global candies
    global step
    candy = int(update.message.text)
    if candy > step:
        update.message.reply_text(f"Берите максимум {step} конфет!", reply_markup=markup2)
        return 1
    else:
        candies -= candy
        if candies <= step:
            update.message.reply_text("Игра окончена. Я забираю оставшиеся конфеты, я победил!", reply_markup=markup)
            return ConversationHandler.END
        else:
            if candies % (step + 1) == 0:
                rand = randint(1, step)
                candies -= rand
                update.message.reply_text(f"Я беру {rand} конфет. Остаётся {candies}. Судя по всему, победа за вами!",
                                          reply_markup=markup2)
            else:
                take = candies % (step + 1)
                candies -= take
                update.message.reply_text(f"Я беру {take}. На кону {candies} конфет", reply_markup=markup2)
            if candies <= step:
                update.message.reply_text("Поздравляю, ты победил!", reply_markup=markup)
                return ConversationHandler.END


def stop(update, context):
    update.message.reply_text("Всего доброго!", reply_markup=markup)
    return ConversationHandler.END


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    settings_hundler = ConversationHandler(
        entry_points=[CommandHandler('settings', settings)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, set_settings)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    play_hundler = ConversationHandler(
        entry_points=[CommandHandler('play', play)],
        states={
            1: [MessageHandler(Filters.text & ~Filters.command, play_step)]
        },
        fallbacks=[CommandHandler('stop', stop)]
    )

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("close", close_keyboard))
    dp.add_handler(settings_hundler)
    dp.add_handler(play_hundler)


    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()