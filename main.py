import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import pyrebase
import fbaseConfig
import classes
import map
from pathlib import Path

updater = Updater('2043960634:AAG-RebQY0pFpdEoD4i6R-eqGybq8Oa3wMM')
firebaseConfig = fbaseConfig.firebaseConfig
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# def updatedb(update: Update, context: CallbackContext) -> None:
#     chat_id = update.message.chat.id
#     new_user = classes.user(update.message.from_user.id, update.message.from_user.username, update.message.from_user.first_name, update.message.from_user.last_name)
#     data = {'username': new_user.username, 'first name': new_user.first_name, 'last name': new_user.last_name}
#     if (len(db.child("users").get().each())) != 0:
#         users = db.child("users").get()
#         for user in users.each():
#             if user_id == int(user.key()):
#                 context.bot.sendMessage(chat_id, "User already exists")
#                 return
#     db.child("users").child(user_id).set(data)
#     context.bot.sendMessage(chat_id, "Successfully added")
#     return

def getroute(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat.id
    map.route()
    path_to_file = 'driving_route_map.jpg'
    path = Path(path_to_file)
    if path.is_file():
        context.bot.sendPhoto(chat_id, photo=open('C:/Users/seans/OneDrive/Documents/GitHub/telegrambotcounter/driving_route_map.jpg', 'rb'))
    else:
        context.bot.sendMessage(chat_id, 'error in getting optimised route')

def getCapacity(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat.id
    bin = db.child("Bin1").get()
    for data in bin.each():
        print(data.val())
    
    

    



# updater.dispatcher.add_handler(CommandHandler('update', updatedb))
# updater.dispatcher.add_handler(CommandHandler('getroute', getroute))
# updater.dispatcher.add_handler(CommandHandler('getCapacity', getCapacity))
# updater.start_polling()
# updater.idle()
    
    
    

