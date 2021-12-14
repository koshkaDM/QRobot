##### Zona de importaciones #####
from telegram.ext import Updater, CommandHandler


### Zona de variables ################
def start(update, context):
    update.message.reply_text(
        'Hola, bienvenido a este bot de prueba creado por @KevinDM... '
        '\n\n ¿Qué desea hacer? \n\n Generar nuevo código QR - /QR')


if __name__ == '__main__':
    updater = Updater(token='5084498276:AAF0FdHkXOSqOJw1VrzwiBiUF1tt3Lg2iUQ', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    updater.start_polling()
    updater.idle()