import telegram
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
from telegram import InlineKeyboardButton,InlineKeyboardMarkup, Update, KeyboardButton,ReplyKeyboardMarkup,Update
import pyrebase
import fbaseConfig
import classes
import map
from pathlib import Path
import main
import capacitymap



def start(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [[
            InlineKeyboardButton("Get Route", callback_data='1'),
            InlineKeyboardButton("Option 2", callback_data='2'),
        ]]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)


def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    query.answer()
    chat_id = query.message.chat.id
    if query.data == '1':
        map.route()
        path_to_file = 'driving_route_map.jpg'
        path = Path(path_to_file)
        if path.is_file():
            context.bot.sendPhoto(chat_id, photo=open('C:/Users/seans/OneDrive/Documents/GitHub/telegrambotcounter/driving_route_map.jpg', 'rb'))
        else:
            context.bot.sendMessage(chat_id, 'error in getting optimised route')
    
    if query.data == '2':
        capacitymap.trash_summary()
        path_to_file = 'WLsummary_Sep-19-2021.png'
        path= Path(path_to_file)
        if path.is_file():
            context.bot.sendPhoto(chat_id, photo=open('C:/Users/seans/OneDrive/Documents/GitHub/telegrambotcounter/WLsummary_Sep-19-2021.png', 'rb'))
        else:
            context.bot.sendMessage(chat_id, 'error in getting trash capacities')
        
        
    query.edit_message_text(text=f"Selected option: {query.data}")


def help_command(update: Update, context: CallbackContext) -> None:
    """Displays info on how to use the bot."""
    update.message.reply_text("Use /start to test this bot.")


def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("2043960634:AAG-RebQY0pFpdEoD4i6R-eqGybq8Oa3wMM")
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_handler(CommandHandler('help', help_command))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()