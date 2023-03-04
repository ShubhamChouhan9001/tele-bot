import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def main():
    # create a new bot instance using the token provided by BotFather
    updater = Updater(token='5671089294:AAFmPY1eRenEjVaRa49YCAQQeKbSnUeJViI', use_context=True)

    # get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # register handlers for commands and messages
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text, calories_counter))

    # start the bot
    updater.start_polling()

    # run the bot until it is stopped
    updater.idle()
