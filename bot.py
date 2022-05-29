################## Zona de importaciones ################################
import os
import qrcode
from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import ChatAction
##########################################################################

######################### Estado cero ##################
INPUT_TEXT = 0
########################################################


###################### Zona de variables #############################
def start(update, context):
    update.message.reply_text(
        'Hola, bienvenido a este bot de prueba creado por @KevinDM... '
        '\n\n ¿Qué desea hacer? \n\n Generar nuevo código QR - /QR')

def qr_command_handler(update, context):
    update.message.reply_text(
        'Muy bien... Ahora envíame el texto que quieres transformar a QR'
    )
    return INPUT_TEXT

def generate_qr(text):
    filename = text + '.jpg'
    img = qrcode.make(text)
    img.save(filename)
    print(filename)
    return filename

def send_qr(filename, chat):
    chat.send_action(
        action=ChatAction.UPLOAD_PHOTO,
        timeout=None
    )
    chat.send_photo(
        photo=open(filename, 'rb')
    )
    os.unlink(filename)

def input_text(update, context):
    text = update.message.text
    print(text)
    filename = generate_qr(text)
    chat = update.message.chat
    print(chat)
    send_qr(filename, chat)
    return ConversationHandler.END
#########################################################################

if __name__ == '__main__':
    updater = Updater(token='YOUR TOKEN HERE', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(ConversationHandler(
        entry_points= [
            CommandHandler('qr', qr_command_handler)
        ],

        states= {
            INPUT_TEXT: [MessageHandler(Filters.text, input_text)]
        },

        fallbacks= []
    ))
    updater.start_polling()
    updater.idle()
