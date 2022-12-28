from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext,  Filters, MessageHandler
import telebot
from telebot import types




def hi_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hi {update.effective_user.first_name}')

def sum_command(update: Update, context: CallbackContext):
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    update.message.reply_text(f'{x} + {y} = {x+y}')

def help_command(update: Update, context: CallbackContext):
    update.message.reply_text(f'/hi\n/sum\n/help')

# def info(update, context):
#     context.bot.
