
########### ==> [Aqui se importa de telegram.ext los elementos CommandHandler y updater] <==##########

from telegram.ext import CommandHandler, Updater

######################################################################################################


############################### ==> [Definiendo funciones] <== ########################################
def start(update, context):
    updater.text.reply_message('Hola, sea bienvenido...')



######################################################################################################
if __name__ == '__main__':

    updater = Updater(token='5084498276:AAF0FdHkXOSqOJw1VrzwiBiUF1tt3Lg2iUQ', use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()
#######################################################################################################