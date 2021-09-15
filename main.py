from telegram import Update
import sqlite3
from telegram.ext import Updater, CommandHandler, CallbackContext

def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')
    print(update.message.from_user.id)
    cursor.execute("INSERT INTO users VALUES({}, 0)".format(update.message.from_user.id))
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print(results)
    
# def zj(update: Update, context: CallbackContext) -> int:
#     update.message.reply_text

connection = sqlite3.connect('telegram_idsAndCounter.db', check_same_thread=False)

cursor = connection.cursor()

# create telegram user table

command1 = """CREATE TABLE IF NOT EXISTS
users(user_id INTEGER PRIMRY KEY, counter INTEGER)"""

cursor.execute(command1)

# add to user db
cursor.execute("INSERT INTO users VALUES(1, 0)")
cursor.execute("SELECT * FROM users")

results = cursor.fetchall()
print(results)

updater = Updater('1985784453:AAGdpA2Drr22_rr7R-VepZ42MzejdUymCIk')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
# updater.dispatcher.add_handler(CommandHandler('Zj', hello))

updater.start_polling()
updater.idle()