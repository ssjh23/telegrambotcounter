import telegram
from telegram import Update
import sqlite3
from telegram.ext import Updater, CommandHandler, CallbackContext
import pyrebase
import fbaseConfig


def updatedb(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    username = update.message.from_user.username
    data = {'user_id': user_id, 'username': username}
    db.child("users").push(data)



updater = Updater('2039559808:AAGgs4QPtIlV_WQ-4__K3BGRTlT8bD7jSV4')
firebaseConfig = fbaseConfig.firebaseConfig
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

updater.dispatcher.add_handler(CommandHandler('update', updatedb))
updater.start_polling()
updater.idle()
    
    
    
    



    
def restrict(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    user_name = context.bot.getChatMember(chat_id = chat_id, user_id=384131105)
    context.bot.restrictChatMember(chat_id = chat_id, user_id=384131105, permissions= telegram.ChatPermissions(can_send_messages=False))
    update.message.reply_text(f'User {user_name.user.username} chat has been restricted')

