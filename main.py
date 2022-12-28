from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, Updater, CallbackContext, Filters, MessageHandler
from pesswort_tok import TOKEN
from bot_command import*
import telebot
from telebot import types

updater = Updater(TOKEN)

# bot = telebot.TeleBot(TOKEN)

# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard= True)
#     item1 = types.KeyboardButton('Приветствие')
#     item2 = types.KeyboardButton('Сложение')
#     item3 = types.KeyboardButton('Какие Команда вводить')
    

#     markup.add(item1, item2, item3)
#     bot.send_message(message, 'hello'.format(message), reply_markup= markup)


updater.dispatcher.add_handler(CommandHandler('hello', hi_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
print('server start')

# bot.polling(non_stop= True)
updater.start_polling()
updater.idle()