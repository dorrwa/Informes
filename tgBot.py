"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

# Chat id 518743443
import asyncio
import requests
import logging
import config
from threading import Thread
from telegram.ext import (Updater, CommandHandler)


def start(update, context):
    ''' START '''
    # Enviar un mensaje a un ID determinado.
    context.bot.send_message(update.message.chat_id, "Bienvenido")


def tgBot():
    TOKEN = config.TGTOKEN
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Eventos que activarán nuestro bot.
    dp.add_handler(CommandHandler('start', start))
    # Comienza el bot
    updater.start_polling()
    # Lo deja a la escucha. Evita que se detenga.
    updater.idle()


if __name__ == '__main__':
    _thread = Thread(target=asyncio.run, args=(tgBot(),))
    _thread.start()
"""
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(update, context):

    update.message.reply_text('Hi!')
def help(update, context):

    update.message.reply_text('Help!')
def echo(update, context):

    update.message.reply_text(update.message.text)
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)
def pizza(update, context):
    if (update.message.text.upper().find("MANZANAS VERDES") > 0):
        update.message.reply_text("Prefiero comer pizza")
def sumar(update, context):
    try:
        numero1 = int(context.args[0])
        numero2 = int(context.args[1])
        suma = numero1 + numero2
        update.message.reply_text("La suma es " + str(suma))
    except (ValueError):
        update.message.reply_text("por favor utilice dos numeros")
def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(config.TGTOKEN, use_context=True)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("sumar", sumar))
    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, pizza))
    # log all errors
    dp.add_error_handler(error)
    # Start the Bot
    updater.start_polling()
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()"""
