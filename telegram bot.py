import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text(
            'Привет {}, я странный чат бот'.format(update.message.from_user.first_name))

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('i cant ')
def textMessage(bot, update):
    response = 'Получил Ваше сообщение: ' + update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=response)

def echo(update, context):
    """Echo the user message."""
    if update.message.text in ("Как дела?", "как дела?", "как дела"):
        update.message.reply_text("Хорошо, а спроси, сколько мне лет?")
    elif update.message.text in ("Привет", "привет"):
        update.message.reply_text("Ну давай, спроси меня как дела?")
    elif update.message.text in ("Сколько тебе лет?", "сколько тебе лет?", "сколько тебе лет"):
        update.message.reply_text("Я точно моложе, чем ты")
    else:
        update.message.reply_text("Я тебя не понимаю")
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater("823915961:AAEjY9XIT-0YdwuNDDPv2PSmMha40OZLlxE", use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
