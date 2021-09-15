import telegram
from telegram import Update
import sqlite3
from telegram.ext import Updater, CommandHandler, CallbackContext


def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hello {update.effective_user.first_name}')
    print(context)
    print(update.message.from_user.id)

def restrict(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    user_name = context.bot.getChatMember(chat_id = chat_id, user_id=39566924)
    context.bot.restrictChatMember(chat_id = chat_id, user_id=39566924, permissions= telegram.ChatPermissions(can_send_messages=False))
    update.message.reply_text(f'User {user_name.user.username} chat has been restricted')

    updater = Updater('1985784453:AAGdpA2Drr22_rr7R-VepZ42MzejdUymCIk')

    updater.dispatcher.add_handler(CommandHandler('hello', hello))
    updater.dispatcher.add_handler(CommandHandler('restrict', restrict))

    updater.start_polling()
    updater.idle()
    # bot.getChatMember

    # update.bot.restrictChatMember(chat_id = chat_id, user_id = 36504923, can_send_messages=False)

    # def main():
    #     connection = sqlite3.connect('telegram_idsAndCounter.db')
    #
    #     cursor = connection.cursor()
    #
    #     # create telegram user table
    #
    #     command1 = """CREATE TABLE IF NOT EXISTS
    #     users(user_id INTEGER PRIMARY KEY, counter INTEGER)"""
    #
    #     cursor.execute(command1)
    #
    #     # add to user db
    #     cursor.execute("INSERT INTO users VALUES(01, 0)")
    #
    #     cursor.execute("SELECT * FROM users")
    #
    #     results = cursor.fetchall()
    #     print(results)