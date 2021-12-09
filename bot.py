from telegram.ext import Updater, CommandHandler

def start(update, context):
    update.message.reply_text('Funciona!!')






if __name__ == '__main__':

    updater = Updater(token='5084498276:AAF0FdHkXOSqOJw1VrzwiBiUF1tt3Lg2iUQ', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()